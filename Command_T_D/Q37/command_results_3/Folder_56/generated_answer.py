import re

def filter_chars(text):
    return re.sub('(?i)[A-Z][^a]*', '', text)