import re

def filter_chars(s):
    return re.sub('<[a-z]>([j-m])<[a-z]', '\x01', s)