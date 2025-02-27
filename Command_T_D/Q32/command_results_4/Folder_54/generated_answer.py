import re

def insert_after_character(s):
    return re.sub('(M)(?=.)', '1f', s)