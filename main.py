import random
import pygame
import time

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

block_color = (random.randrange(0, 254), random.randrange(0, 254), random.randrange(0, 254))

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Racey")
clock = pygame.time.Clock()

car_img = pygame.image.load("car.png")
car_img = pygame.transform.scale(car_img, (100, 160))


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(count), True, black)
    game_display.blit(text, (0, 0))


def things(x, y, width, height, color):
    pygame.draw.rect(game_display, color, [x, y, width, height])


def car(x, y):
    game_display.blit(car_img, (x, y))


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()


def message_display(text):
    large_text = pygame.font.Font("freesansbold.ttf", 115)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((display_width / 2), (display_height / 2))
    game_display.blit(text_surf, text_rect)

    pygame.display.update()
    time.sleep(2)
    game_loop()


def crash():
    message_display("You crashed")


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.7)

    x_change = 0
    thing_width = 100
    thing_height = 100
    thing_startx = random.randrange(0, display_width - thing_width)
    thing_starty = -600
    thing_speed = 7

    dodged = 0

    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -10
                elif event.key == pygame.K_RIGHT:
                    x_change = 10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        game_display.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)

        if x > display_width - 100 or x < 0:
            crash()
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width - thing_width)
            dodged += 1
            thing_speed += 1
            thing_width += 10

        if y < thing_starty + thing_height:
            if x + 100 > thing_startx and x < thing_startx + thing_width:
                crash()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
