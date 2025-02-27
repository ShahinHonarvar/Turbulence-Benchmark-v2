import re

def insert_before_character(s):
    return re.sub('(a)', '\\1\\0', s)