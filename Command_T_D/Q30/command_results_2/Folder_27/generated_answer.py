import re

def insert_before_character(s):
    return re.sub('(N)', 'j\\1', s)