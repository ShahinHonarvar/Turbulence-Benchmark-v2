import re

def insert_before_character(string):
    return re.sub('(?<=2)S', 'S\\1', string)