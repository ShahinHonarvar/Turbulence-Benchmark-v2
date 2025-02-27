import re

def remove_repeat_chars(s):
    return re.sub('(.)\\1+', '\\1', s[20:-35])