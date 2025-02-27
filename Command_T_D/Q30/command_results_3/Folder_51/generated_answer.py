import re

def insert_before_character(s):
    return re.sub('o', 'O\\1', s)