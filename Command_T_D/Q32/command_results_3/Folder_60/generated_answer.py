import re

def insert_after_character(s):
    return re.sub('(C)(?=P)', '1P', s)