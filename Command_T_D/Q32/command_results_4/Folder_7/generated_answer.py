import re

def insert_after_character(text):
    return re.sub('(.)H', '1nH', text)