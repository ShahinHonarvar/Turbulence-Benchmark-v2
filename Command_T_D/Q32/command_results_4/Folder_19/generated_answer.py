import re

def insert_after_character(text):
    return re.sub('5(?!h)', '5h', text)