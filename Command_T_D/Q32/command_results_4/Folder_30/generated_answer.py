import re

def insert_after_character(text):
    return re.sub('4(?!F)', '4F', text)