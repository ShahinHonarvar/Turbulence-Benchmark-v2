import re

def filter_chars(text):
    return re.sub('[a-h]([A-e])', '\x01', text)