import re

def insert_after_character(s):
    return re.sub('u', 'u\\1', s)