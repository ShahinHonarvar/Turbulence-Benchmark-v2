import re

def insert_after_character(s):
    return re.sub('6(?!9)', '66', s)