import re

def filter_chars(str1):
    return re.sub('([%\\d])', '', str1)