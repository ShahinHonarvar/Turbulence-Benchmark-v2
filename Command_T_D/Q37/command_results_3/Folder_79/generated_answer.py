import re

def filter_chars(s):
    return re.sub('(?<=.)@(.*?)\x01T', '', s)