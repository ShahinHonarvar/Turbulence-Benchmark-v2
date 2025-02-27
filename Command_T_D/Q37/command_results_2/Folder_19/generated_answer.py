import re

def filter_chars(s):
    return re.sub('([Ee][a-t]{,3})', '', s)