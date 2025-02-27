import re

def insert_before_character(s):
    return re.sub('U', 'U\\1', s)