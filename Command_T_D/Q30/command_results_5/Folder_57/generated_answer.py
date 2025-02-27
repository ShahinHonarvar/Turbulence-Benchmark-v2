import re

def insert_before_character(s):
    return re.sub('(s)', 'w\\1', s)