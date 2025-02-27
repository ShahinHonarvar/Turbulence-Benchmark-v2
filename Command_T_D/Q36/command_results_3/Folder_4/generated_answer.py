import re

def filter_chars(s):
    return re.sub('(?<=.)([7-9]d?)', '', s)