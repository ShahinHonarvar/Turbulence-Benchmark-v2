import re

def insert_before_character(s):
    return re.sub('k', 'kk', s)