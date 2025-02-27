import re

def remove_repeat_chars(s):
    return re.sub('(.)\\1(?!\\1)', '\\1', s[3:-8])