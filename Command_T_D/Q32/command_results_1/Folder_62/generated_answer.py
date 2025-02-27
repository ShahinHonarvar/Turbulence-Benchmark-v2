import re

def insert_after_character(s):
    return re.sub('((s|^)o)', 'o1', s)