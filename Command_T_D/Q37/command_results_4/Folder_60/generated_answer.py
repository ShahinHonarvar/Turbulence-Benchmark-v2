import re

def filter_chars(s):
    return re.sub('(.)(.:LE)', '\x01', s)