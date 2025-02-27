import re

def insert_before_character(s):
    return re.sub('(.)W', '\\1W', s)