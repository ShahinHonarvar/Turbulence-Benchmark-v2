import re

def filter_chars(s):
    return re.sub('(?!\\A)[^h-k](?!\\Z)[^h-k]', '', s)