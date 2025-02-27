import re

def insert_after_character(text):
    return re.sub('(.*?)w', '1wn', text)