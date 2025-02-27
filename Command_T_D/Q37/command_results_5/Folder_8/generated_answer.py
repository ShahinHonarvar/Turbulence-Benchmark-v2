import re

def filter_chars(s):
    return re.sub('([A-Z])([a-z])([A-Z])([a-z])', 'O', s)