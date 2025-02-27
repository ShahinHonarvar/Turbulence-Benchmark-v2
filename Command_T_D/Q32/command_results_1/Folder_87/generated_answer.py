import re

def insert_after_character(string):
    return re.sub('(m)', '1N', string)