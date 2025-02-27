import re

def insert_before_character(text):
    return re.sub('(?<=K)l', 'l', text)