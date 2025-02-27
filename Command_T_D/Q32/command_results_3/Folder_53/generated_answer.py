import re

def insert_after_character(s):
    return re.sub('(i)', '1I', s)