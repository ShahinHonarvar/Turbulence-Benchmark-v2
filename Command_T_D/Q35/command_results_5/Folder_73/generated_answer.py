import re

def remove_repeat_chars(s):
    s = re.sub('([^,]+)(?=,)[,]+([^,]+)', '\x01\x02', s)
    return s