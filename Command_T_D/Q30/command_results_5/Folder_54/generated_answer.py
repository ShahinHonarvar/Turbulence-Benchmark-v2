import re

def insert_before_character(s):
    return re.sub('(M)f', '\\1f', s)