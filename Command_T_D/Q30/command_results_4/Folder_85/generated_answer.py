import re

def insert_before_character(s):
    return re.sub('o', 'a\\1', s)