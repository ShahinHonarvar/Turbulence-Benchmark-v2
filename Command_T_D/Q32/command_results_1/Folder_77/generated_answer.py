import re

def insert_after_character(s):
    return re.sub('9(?!h)', '9h', s)