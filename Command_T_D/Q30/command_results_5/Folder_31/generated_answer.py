import re

def insert_before_character(text):
    return re.sub('(?<=B)N', 'N\\1', text)