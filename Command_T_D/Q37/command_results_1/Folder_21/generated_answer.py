import re

def filter_chars(text):
    return re.sub('[qhq]([a-z])', '\x01', text)