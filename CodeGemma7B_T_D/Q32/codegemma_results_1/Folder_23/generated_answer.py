import re

def insert_after_character(s):
    return re.sub('(b)([^b]*)', '\\\\1y\\\\2', s)