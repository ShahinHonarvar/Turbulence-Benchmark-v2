import re

def insert_before_character(text):
    return re.sub('(?<=0)H0', 'H0', text)