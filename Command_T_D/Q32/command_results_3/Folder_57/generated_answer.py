import re

def insert_after_character(text):
    return re.sub('s(?!w)', 'sw', text)