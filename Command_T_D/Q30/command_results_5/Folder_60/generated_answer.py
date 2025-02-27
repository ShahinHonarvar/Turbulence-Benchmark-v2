import re

def insert_before_character(s):
    return re.sub('(C)(?=P)', '\\1P', s)