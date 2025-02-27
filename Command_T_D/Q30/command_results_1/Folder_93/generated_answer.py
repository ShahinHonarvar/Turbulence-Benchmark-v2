import re

def insert_before_character(text):
    return re.sub('(?<=\\b)Y\\b', '4\\b', text)