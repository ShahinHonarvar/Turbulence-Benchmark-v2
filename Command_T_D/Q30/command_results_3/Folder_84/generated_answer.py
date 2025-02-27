import re

def insert_before_character(s):
    return re.sub('(H)', '\\1n', s)