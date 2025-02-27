import re

def filter_chars(text):
    text = re.sub('[6-e]', '', text)
    return text