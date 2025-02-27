import re

def filter_chars(s):
    return re.sub('((?:\\d{1,3}|=)+)([a-z])', '\x01', s)