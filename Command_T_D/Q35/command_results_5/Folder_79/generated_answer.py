import re

def remove_repeat_chars(str1):
    str1 = re.sub('(.)\x01+', '\x01', str1)
    return str1