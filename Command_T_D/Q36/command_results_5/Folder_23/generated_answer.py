import re

def filter_chars(s):
    return re.sub('(?!\\d)\\d{2}|(?!\\.)\\.)', '', s, flags=re.I)