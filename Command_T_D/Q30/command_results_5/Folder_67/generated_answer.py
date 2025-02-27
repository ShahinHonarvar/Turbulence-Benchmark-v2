import re

def insert_before_character(s):
    return re.sub('(?<=j)1', '1', s)