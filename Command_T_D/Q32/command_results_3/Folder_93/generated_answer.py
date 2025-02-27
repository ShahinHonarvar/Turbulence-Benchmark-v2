import re

def insert_after_character(s):
    return re.sub('(?<=Y)4', '4', s)