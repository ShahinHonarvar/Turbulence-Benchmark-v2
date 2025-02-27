import re

def insert_after_character(s):
    return re.sub('(E)(?=T)', '\\1T', s)