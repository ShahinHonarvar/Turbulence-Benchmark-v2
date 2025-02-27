import re

def filter_chars(s):
    return re.sub('([D-H])', '5', s)