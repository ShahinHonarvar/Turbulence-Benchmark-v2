import re

def insert_after_character(text):
    return re.sub('I(?!i)', 'I1i', text)