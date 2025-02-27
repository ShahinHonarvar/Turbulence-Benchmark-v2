import re

def filter_chars(s):
    return re.sub('(?<=.)4-5.[7-o]', '', s)