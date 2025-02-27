import re

def insert_after_character(s):
    return re.sub('(.)\\s', '\\1 \\2', s)