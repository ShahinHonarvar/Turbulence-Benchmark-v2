import re

def insert_after_character(s):
    return re.sub('a', '6\\1', s)