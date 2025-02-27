import re

def insert_after_character(s):
    return re.sub('U(?!u)', 'U1u', s)