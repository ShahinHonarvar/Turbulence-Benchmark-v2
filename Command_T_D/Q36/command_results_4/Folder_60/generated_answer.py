import re

def filter_chars(s):
    return re.sub('([a-zA-Z])\x08(g-o)\x08([a-zA-Z])', '\x01\x02\x03', s)