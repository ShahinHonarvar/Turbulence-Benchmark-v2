import re

def insert_after_character(s):
    return re.sub('(k)', 'k1', s)