import re

def insert_before_character(s):
    return re.sub('(6)', '\\1 9', s)