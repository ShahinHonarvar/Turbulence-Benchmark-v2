import re

def insert_after_character(s):
    return re.sub('(.)H', '1HH', s)