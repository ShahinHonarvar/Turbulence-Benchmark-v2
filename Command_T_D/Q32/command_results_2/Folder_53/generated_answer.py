import re

def insert_after_character(s):
    return re.sub('(i)', 'I1', s)