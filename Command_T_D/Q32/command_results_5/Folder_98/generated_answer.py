import re

def insert_after_character(string):
    return re.sub('U', 'u1', string)