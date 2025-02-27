import re

def filter_chars(text):
    return re.sub('(?i)([jve])', '\\1', text)