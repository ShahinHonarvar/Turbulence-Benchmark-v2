import re

def insert_before_character(string):
    return re.sub('U', 'u\\1', string)