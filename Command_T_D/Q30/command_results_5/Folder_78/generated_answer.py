import re

def insert_before_character(s):
    return re.sub('(H)(?=s)', '\\1s', s)