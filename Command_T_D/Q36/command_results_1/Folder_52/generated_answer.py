import re

def filter_chars(s):
    return re.sub('(?<![a-z]){49,56}(?=[a-z])', '', s)