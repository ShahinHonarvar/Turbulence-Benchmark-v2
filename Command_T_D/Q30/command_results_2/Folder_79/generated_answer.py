import re

def insert_before_character(s):
    return re.sub('(E)', 'E\x01', s)