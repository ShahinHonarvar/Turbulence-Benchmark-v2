import re

def insert_before_character(s):
    return re.sub('j', 'v\\1', s)