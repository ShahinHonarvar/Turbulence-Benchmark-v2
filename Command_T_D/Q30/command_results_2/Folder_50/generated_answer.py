import re

def insert_before_character(s):
    return re.sub('t', 'u\\1', s)