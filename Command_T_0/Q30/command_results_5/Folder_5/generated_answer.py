import re

def insert_before_character(s):
    return re.sub('(c)', 'G\\1', s)