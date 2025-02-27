import re

def insert_after_character(s):
    return re.sub('(.)5', '\\1\\5', s)