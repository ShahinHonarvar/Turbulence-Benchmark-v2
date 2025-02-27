import re

def filter_chars(s):
    return re.sub('(A[a-z])', 'A\x01', s)