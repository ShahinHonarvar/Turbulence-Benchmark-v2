import re

def filter_chars(s):
    return re.sub('([\\d\\w])>[\\d\\w]', '\x01', s)