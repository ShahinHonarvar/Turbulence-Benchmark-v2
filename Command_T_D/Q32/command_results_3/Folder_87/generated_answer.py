import re

def insert_after_character(s):
    return re.sub('m', 'mN', s)