import re

def insert_before_character(s):
    return re.sub('x', 'N\\x', s)