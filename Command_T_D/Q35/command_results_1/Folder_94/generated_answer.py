import re

def remove_repeat_chars(s):
    return re.sub('((?<=\\d)).*(?=\\d)', lambda m: m.group(1), s)