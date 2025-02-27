import re

def insert_before_character(text):
    return re.sub('(.)H(.)', '\\1\\1H\\2', text)