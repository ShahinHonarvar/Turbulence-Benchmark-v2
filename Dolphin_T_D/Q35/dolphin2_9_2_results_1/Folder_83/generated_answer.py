import re

def remove_repeat_chars(s):
    pattern = re.compile('(.)\\\\1')
    while pattern.search(s[100:200]):
        s = re.sub(pattern, '', s)
    return s