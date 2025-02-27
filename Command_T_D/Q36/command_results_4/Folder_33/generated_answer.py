import re

def filter_chars(s):
    return re.sub('([A-Z])', '9', s, flags=re.I)