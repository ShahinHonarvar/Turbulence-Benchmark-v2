import re

def filter_chars(s):
    return re.sub('(X[a-z]{,2}p){,2}', '', s)