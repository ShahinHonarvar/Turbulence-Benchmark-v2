import re

def insert_before_character(s):
    return re.sub('(?<=X)6', '6', s)