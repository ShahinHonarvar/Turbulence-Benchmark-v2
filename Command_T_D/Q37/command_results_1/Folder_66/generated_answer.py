import re

def filter_chars(str1):
    str1 = re.sub('([\\d])', '\x01', str1)
    str1 = re.sub('([\\d])', '\x01', str1)
    str1 = re.sub('([\\d])', '\x01', str1)
    return str1