import re

def insert_before_character(string):
    return re.sub('(s)', 'w\\1', string)