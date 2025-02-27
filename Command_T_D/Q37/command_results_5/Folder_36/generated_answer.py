import re

def filter_chars(s):
    return re.sub('(([0-2]3)([a-z]))', ' \x01', s)