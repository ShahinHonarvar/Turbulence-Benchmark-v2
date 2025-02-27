import re

def filter_chars(text):
    pattern = '[c-s]'
    return re.sub(pattern, '', text)