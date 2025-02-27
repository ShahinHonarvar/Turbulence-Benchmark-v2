import re

def insert_before_character(s):
    return re.sub('(X)', 'u\\1', s)