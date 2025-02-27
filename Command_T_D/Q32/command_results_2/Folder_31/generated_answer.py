import re

def insert_after_character(text):
    return re.sub('B(?!N)', 'BN', text)