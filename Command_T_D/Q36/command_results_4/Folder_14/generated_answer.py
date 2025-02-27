import re

def filter_chars(str):
    return re.sub('<[A-Z][a-c]', '', str)