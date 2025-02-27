import re

def insert_after_character(s):
    return re.sub('(Y)(?=\\d)', 'Y4', s)