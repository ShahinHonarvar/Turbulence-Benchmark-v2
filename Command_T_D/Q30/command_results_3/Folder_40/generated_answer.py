import re

def insert_before_character(text):
    return re.sub('e', 'e\x01', text)