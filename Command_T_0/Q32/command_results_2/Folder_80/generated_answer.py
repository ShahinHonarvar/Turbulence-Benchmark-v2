import re

def insert_after_character(s):
    return re.sub('(.)X', '\\1X', s)