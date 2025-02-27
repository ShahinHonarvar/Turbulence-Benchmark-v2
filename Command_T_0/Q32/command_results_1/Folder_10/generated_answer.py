import re

def insert_after_character(s):
    return re.sub('(j)', 'v\\1', s)