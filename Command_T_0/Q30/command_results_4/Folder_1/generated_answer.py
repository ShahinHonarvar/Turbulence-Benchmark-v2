import re

def insert_before_character(s):
    return re.sub('U', 'T\\1', s)