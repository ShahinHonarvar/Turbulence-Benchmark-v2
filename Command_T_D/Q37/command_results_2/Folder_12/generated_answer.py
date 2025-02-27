import re

def filter_chars(s):
    return re.sub('(?<=\x08[fgh])([fgh])', '', s)