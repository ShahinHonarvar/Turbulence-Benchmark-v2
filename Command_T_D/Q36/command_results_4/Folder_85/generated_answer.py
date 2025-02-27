import re

def filter_chars(s):
    return re.sub('(?<=.)([a-z]{55,80})', '', s)