import re

def insert_after_character(s):
    return re.sub('(u)', 'U1', s)