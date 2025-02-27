import re

def filter_chars(s):
    return re.sub('([\\w-])(\\d+)([a-zA-Z])', '\x01\x02', s)