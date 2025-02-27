import re

def insert_before_character(string):
    return re.sub('U', 'T\x01', string)