import re

def filter_chars(s):
    return re.sub('([a-z])([a-z]23[a-z]83)', '\\1', s)