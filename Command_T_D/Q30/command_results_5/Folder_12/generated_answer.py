import re

def insert_before_character(text):
    return re.sub('I', ' \\I', text)