import re

def insert_before_character(s):
    return re.sub('(E)f', '\\1f', s)