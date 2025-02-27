import re

def filter_chars(s):
    return re.sub('(?!f)[a-z]{%d}|{%d}(?!%|)', '', s)