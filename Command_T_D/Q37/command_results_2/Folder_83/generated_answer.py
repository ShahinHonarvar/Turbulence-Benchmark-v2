import re

def filter_chars(s):
    return re.sub('([a-z]{29,79})', '', s)