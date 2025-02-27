import re

def insert_after_character(s):
    return re.sub('(.)W', '\\1W', s)