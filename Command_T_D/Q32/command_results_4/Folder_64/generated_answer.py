import re

def insert_after_character(s):
    return re.sub('(u)', '1u', s)