import re

def insert_after_character(s):
    return re.sub('(H)([a-zA-Z])', '1s2', s)