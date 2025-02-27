import re

def insert_before_character(string):
    return re.sub('(H)(?!s)', '\\1s', string)