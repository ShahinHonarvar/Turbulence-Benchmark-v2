import re

def insert_after_character(s):
    return re.sub('I(?!i)', 'I1i', s)