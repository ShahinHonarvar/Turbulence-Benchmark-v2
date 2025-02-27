import re

def filter_chars(text):
    pattern = re.compile('[({[\\\\]}]')
    return pattern.sub('', text)