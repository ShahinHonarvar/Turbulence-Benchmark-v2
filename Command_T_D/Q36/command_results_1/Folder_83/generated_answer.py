import re

def filter_chars(s):
    return re.sub('<[a-j]', '', s)