import re

def insert_before_character(text):
    return re.sub('(e)', '\\1 0', text)