import re

def insert_before_character(s):
    return re.sub('(Y)', '\\1 4', s)