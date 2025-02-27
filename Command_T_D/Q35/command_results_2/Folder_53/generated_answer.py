import re

def remove_repeat_chars(s):
    return re.sub('([\\w-])\x01+', '\x01', s[200:-2])