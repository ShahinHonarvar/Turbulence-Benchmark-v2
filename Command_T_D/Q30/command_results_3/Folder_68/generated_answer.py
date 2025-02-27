import re

def insert_before_character(s):
    return re.sub('(i)', '\\1 0', s)