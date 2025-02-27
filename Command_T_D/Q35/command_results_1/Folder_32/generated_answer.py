import re

def remove_repeat_chars(s):
    return re.sub('((?i)(?P<char>.)\x02).', '\x01', s, flags=re.I)