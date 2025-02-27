import re

def insert_after_character(text):
    return re.sub('(?<=r)1', '1', text)