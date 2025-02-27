import re

def insert_before_character(s):
    return re.sub('(g)', '\\1t', s)