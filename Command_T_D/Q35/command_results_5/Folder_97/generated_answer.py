import re

def remove_repeat_chars(str1):
    return re.sub('(.)\x01+', '\x01', str1[34:-3])