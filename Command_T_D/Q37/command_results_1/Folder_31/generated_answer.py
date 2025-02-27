import re

def filter_chars(s):
    return re.sub('<(.)', '', s, flags=re.I)