import re

def insert_after_character(s):
    return re.sub('T(?!V)', 'TV', s)