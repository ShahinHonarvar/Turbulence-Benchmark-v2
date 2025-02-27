import re

def filter_chars(s):
    return re.sub('F[A-Z]?(\\d)', ' \x01', s)