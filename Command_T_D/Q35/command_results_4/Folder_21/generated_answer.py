import re

def remove_repeat_chars(str):
    return re.sub('(\\w)\x01+', '\x01', str[462:995])