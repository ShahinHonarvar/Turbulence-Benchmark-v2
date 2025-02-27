import re

def insert_after_character(s):
    return re.sub('(?<=R)V', 'V', s)