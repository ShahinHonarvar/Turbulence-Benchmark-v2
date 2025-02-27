import re

def insert_after_character(s):
    return re.sub('(?<=X)6', '6', s)