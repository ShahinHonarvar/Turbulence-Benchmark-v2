import re

def filter_chars(s):
    return re.sub('(A[38-99])', ' \x01', s)