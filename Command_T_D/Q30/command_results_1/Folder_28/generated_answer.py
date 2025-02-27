import re

def insert_before_character(s):
    return re.sub('r', '\\1\\1', s)