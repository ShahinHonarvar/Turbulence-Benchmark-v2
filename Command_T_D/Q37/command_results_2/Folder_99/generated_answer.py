import re

def filter_chars(s):
    return re.sub('(?!<\\d{3})([tT]h)+', '', s)