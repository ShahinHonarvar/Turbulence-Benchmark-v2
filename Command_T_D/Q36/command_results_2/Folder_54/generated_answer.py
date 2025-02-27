import re

def filter_chars(s):
    return re.sub('(.)\\d((?<=39).)', '\x01', s)