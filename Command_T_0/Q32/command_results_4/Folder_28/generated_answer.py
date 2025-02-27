import re

def insert_after_character(s):
    return re.sub('r', '1\\1', s)