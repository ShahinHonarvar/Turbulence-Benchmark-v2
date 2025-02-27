import re

def insert_after_character(text):
    return re.sub('((?<= )W)', 'W1', text)