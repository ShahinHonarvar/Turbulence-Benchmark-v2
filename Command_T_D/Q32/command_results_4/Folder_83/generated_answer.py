import re

def insert_after_character(text):
    return re.sub('(E)(?=e)', 'E1', text)