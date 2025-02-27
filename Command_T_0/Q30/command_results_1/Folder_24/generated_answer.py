import re

def insert_before_character(s):
    return re.sub('0', '4\\0', s)