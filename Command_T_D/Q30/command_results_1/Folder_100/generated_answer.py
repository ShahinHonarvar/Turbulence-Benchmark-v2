import re

def insert_before_character(s):
    return re.sub('0', '\\1 \\0', s)