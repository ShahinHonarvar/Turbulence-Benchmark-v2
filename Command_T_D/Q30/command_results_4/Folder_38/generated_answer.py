import re

def insert_before_character(text):
    return re.sub('(?<=X)6', '6', text)