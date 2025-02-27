import re

def insert_before_character(s):
    return re.sub('(Y)', '4\\1', s)