import re

def insert_before_character(s):
    return re.sub('e', '0e', s)