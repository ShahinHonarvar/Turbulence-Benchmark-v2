import re

def insert_before_character(text):
    return re.sub('(e)', 'E\\1', text)