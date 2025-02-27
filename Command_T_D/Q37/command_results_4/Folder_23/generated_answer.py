import re

def filter_chars(s):
    return re.sub('<(V|v)+(Y|y)+>', '', s)