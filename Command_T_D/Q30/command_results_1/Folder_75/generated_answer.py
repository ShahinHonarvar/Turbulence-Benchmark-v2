import re

def insert_before_character(s):
    return re.sub('U', 'Uq', s)