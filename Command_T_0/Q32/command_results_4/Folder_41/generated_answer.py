import re

def insert_after_character(s):
    return re.sub('O', 'o\\1', s)