import re

def insert_after_character(text):
    return re.sub('(E)', '1E', text)