import re

def insert_after_character(s):
    return re.sub('e', 'e0', s)