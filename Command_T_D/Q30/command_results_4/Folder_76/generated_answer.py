import re

def insert_before_character(text):
    return re.sub('F', 'mF', text)