import re

def filter_chars(s):
    return re.sub('([^Ys]?)', '', s, flags=re.I)