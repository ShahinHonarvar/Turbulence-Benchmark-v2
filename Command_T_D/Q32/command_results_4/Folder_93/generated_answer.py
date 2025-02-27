import re

def insert_after_character(text):
    return re.sub('(?<=Y)4', '4', text)