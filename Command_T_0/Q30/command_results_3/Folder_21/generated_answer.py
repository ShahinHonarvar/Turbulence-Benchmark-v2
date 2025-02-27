import re

def insert_before_character(s):
    return re.sub('(.)\\s', '\\1K\\s', s)