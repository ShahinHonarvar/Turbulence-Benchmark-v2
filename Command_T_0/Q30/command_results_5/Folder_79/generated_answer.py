import re

def insert_before_character(s):
    return re.sub('(E)', 'E\\1', s)