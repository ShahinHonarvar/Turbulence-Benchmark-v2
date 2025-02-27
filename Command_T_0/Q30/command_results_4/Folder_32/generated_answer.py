import re

def insert_before_character(s):
    return re.sub('F', 'u\\1', s)