import re

def insert_before_character(s):
    return re.sub('(e)', '\\1\\0', s)