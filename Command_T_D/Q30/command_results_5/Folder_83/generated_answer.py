import re

def insert_before_character(s):
    return re.sub('(E)', 'e\\1', s)