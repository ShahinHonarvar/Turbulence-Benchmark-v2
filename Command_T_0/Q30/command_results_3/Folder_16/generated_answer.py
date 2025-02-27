import re

def insert_before_character(s):
    return re.sub('(.)w', '\\1n\\2', s)