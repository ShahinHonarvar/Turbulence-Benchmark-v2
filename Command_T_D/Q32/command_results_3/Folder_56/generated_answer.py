import re

def insert_after_character(s):
    return re.sub('(I)', '1i', s)