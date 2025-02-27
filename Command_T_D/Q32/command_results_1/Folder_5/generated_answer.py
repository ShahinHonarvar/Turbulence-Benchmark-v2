import re

def insert_after_character(s):
    return re.sub('c', 'cG', s)