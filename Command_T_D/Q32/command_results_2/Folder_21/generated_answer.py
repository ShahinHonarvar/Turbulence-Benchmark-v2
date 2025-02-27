import re

def insert_after_character(s):
    return re.sub('(.)K(.)', '1K2', s)