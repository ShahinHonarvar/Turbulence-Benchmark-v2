import re

def insert_after_character(text):
    return re.sub('(?<=i)0', '0', text)