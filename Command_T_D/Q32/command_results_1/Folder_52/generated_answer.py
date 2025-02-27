import re

def insert_after_character(text):
    return re.sub('(T)V', '1V', text)