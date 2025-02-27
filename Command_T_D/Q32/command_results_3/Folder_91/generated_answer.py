import re

def insert_after_character(string):
    return re.sub('a(?!0)', 'a0', string)