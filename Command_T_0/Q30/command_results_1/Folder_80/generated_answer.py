import re

def insert_before_character(s):
    return re.sub('(.)X', '\\1X', s)