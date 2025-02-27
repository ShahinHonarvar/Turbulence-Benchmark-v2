import re

def filter_chars(s):
    return re.sub('([A-Z])', '3', s, flags=re.I)