import re

def insert_after_character(text):
    return re.sub('(?<=T) ', 'T', text)