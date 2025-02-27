import re

def filter_chars(str):
    return re.sub('(3[a-d]*)', '\x01', str)