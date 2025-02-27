import re

def insert_before_character(s):
    return re.sub('Q', 'I\\1', s)