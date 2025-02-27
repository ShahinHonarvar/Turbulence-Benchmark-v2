import re

def filter_chars(s):
    return re.sub('<(c) ([A-Z])', '\x01', s)