import re

def insert_before_character(text):
    return re.sub('(S)', '\\1U', text)