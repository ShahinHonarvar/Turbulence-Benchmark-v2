import re

def filter_chars(s):
    return re.sub('([^Y]s)', '', s)