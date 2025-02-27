import re

def insert_before_character(string):
    return re.sub('F', 'u\\1', string)