import re

def filter_chars(s):
    return re.sub('([fho])([19-32])', '\x01', s)