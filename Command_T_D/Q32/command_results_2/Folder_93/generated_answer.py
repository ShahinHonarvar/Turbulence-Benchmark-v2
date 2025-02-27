import re

def insert_after_character(s):
    return re.sub('(.*?)Y', '1 4', s)