import re

def filter_chars(s):
    return re.sub('(?!\\?)([a-z])([^a-z\\?]{%d}){%d}(?!k)', '\x01', s)