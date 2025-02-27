import re

def filter_chars(s):
    return re.sub('(?!s)[a-z]cdeflgjklmnpqrstu', '', s)