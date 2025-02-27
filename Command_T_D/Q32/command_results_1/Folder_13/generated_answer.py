import re

def insert_after_character(s):
    return re.sub('x(?!N)', 'xN', s)