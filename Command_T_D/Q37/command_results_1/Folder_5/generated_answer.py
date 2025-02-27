import re

def filter_chars(s):
    return re.sub('<[5-]=82', '', s)