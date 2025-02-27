import re

def insert_after_character(text):
    return re.sub('(u)', '1u', text)