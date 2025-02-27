import re

def insert_after_character(text):
    return re.sub('(.)s+', '1Hs+', text)