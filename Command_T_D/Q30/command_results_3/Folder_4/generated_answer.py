import re

def insert_before_character(text):
    return re.sub('(?<=a)6', '6', text)