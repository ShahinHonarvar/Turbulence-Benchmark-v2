import re

def insert_before_character(s):
    return re.sub('(?<=.)5', '\\1', s)