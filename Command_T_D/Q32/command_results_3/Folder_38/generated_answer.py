import re

def insert_after_character(text):
    return re.sub('(?<=X)6', '6', text)