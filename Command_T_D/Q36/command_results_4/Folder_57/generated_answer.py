import re

def filter_chars(str1):
    str1 = re.sub('([A-Z])', ' \x01', str1)
    str1 = re.sub('([a-z])([A-Z])', '\x01 \x02', str1)
    return str1