import re

def insert_before_character(s):
    return re.sub('j', '1j', s)