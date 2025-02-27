import re

def insert_after_character(text):
    return re.sub('(.)X', '1XX', text)