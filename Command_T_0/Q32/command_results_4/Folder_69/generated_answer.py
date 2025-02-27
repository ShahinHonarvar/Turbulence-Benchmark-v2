import re

def insert_after_character(s):
    return re.sub('(.)P', '\\1P', s)