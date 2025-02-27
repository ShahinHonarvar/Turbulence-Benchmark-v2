import re

def insert_before_character(s):
    return re.sub('(M)', 'f\x01', s)