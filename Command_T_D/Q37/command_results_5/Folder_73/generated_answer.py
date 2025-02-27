import re

def filter_chars(s):
    return re.sub('([7-e])([22-85])', '\x01\x02', s)