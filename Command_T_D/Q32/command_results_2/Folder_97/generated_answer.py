import re

def insert_after_character(s):
    return re.sub('o(?!h)', 'oh', s)