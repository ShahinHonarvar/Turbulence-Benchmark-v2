import re

def insert_before_character(s):
    return re.sub('(S)', 'U\\1', s)