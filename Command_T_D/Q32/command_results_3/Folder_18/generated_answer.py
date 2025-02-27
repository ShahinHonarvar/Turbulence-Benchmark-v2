import re

def insert_after_character(s):
    return re.sub('K(?!l)', 'KL', s)