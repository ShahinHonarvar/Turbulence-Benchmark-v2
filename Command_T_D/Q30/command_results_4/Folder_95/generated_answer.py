import re

def insert_before_character(text):
    return re.sub('(?<=j)q', 'q', text)