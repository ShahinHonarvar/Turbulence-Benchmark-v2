import re

def insert_before_character(s):
    return re.sub('(e)', 'e\\1', s)