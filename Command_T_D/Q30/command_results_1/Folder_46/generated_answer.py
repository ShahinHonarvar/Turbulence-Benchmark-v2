import re

def insert_before_character(s):
    return re.sub('(?<=6)W', 'W\\1', s)