import re

def insert_after_character(text):
    return re.sub('(.)', '1 2', text)