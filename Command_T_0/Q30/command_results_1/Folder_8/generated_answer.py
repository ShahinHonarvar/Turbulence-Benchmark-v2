import re

def insert_before_character(s):
    return re.sub('(E)', 'T\\1', s)