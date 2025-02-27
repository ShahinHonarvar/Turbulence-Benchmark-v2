import re

def insert_after_character(s):
    return re.sub('S(?!U)', 'SU', s)