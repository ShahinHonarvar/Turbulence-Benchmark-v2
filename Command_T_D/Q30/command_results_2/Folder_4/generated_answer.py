import re

def insert_before_character(s):
    return re.sub('(?<=a)6', 'a6', s)