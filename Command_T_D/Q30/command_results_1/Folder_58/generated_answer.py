import re

def insert_before_character(s):
    return re.sub('(?<=F)o', 'o', s)