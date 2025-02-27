import re

def insert_before_character(string):
    return re.sub('(a)', 'a\\1', string)