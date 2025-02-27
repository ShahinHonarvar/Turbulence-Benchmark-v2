import re

def insert_after_character(text):
    return re.sub('(e)([a-z])', '1E2', text)