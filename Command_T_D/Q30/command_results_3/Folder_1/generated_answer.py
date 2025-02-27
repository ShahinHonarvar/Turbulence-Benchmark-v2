import re

def insert_before_character(string):
    return re.sub('U', 'T\\1', string)