import re

def insert_before_character(s):
    return re.sub('(?<=.)o', 'o', s)