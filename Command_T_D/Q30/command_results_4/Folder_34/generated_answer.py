import re

def insert_before_character(s):
    return re.sub('(A)', 'a\\1', s)