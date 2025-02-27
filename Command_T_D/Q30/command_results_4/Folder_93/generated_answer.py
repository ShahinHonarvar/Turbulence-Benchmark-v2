import re

def insert_before_character(text):
    return re.sub('(?!4)Y', '4Y', text)