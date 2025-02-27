import re

def remove_repeat_chars(s):
    return re.sub('(\\S*)([A-Z][^A-Z]*)([A-Z])', '\x01\x02', s)