import re

def insert_before_character(s):
    return re.sub('a', 'n\\a', s)