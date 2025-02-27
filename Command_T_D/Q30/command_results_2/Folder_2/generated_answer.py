import re

def insert_before_character(s):
    return re.sub('(C)', 'Z\\1', s)