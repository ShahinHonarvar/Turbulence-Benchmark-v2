import re

def insert_after_character(text):
    return re.sub('F(.)', 'FO1', text)