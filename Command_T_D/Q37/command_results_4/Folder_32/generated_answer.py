import re

def filter_chars(s):
    return re.sub('(w[a-z])', '', s)