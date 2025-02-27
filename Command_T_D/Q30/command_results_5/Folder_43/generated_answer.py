import re

def insert_before_character(s):
    return re.sub('t', 'G\\1', s)