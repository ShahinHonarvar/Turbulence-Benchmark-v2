import re

def filter_chars(s):
    return re.sub('([A-Q]{38,99})', '', s)