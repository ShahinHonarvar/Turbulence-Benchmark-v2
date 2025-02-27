import re

def insert_before_character(s):
    return re.sub('r', 'w\\1', s)