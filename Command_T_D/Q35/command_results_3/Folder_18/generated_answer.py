import re

def remove_repeat_chars(str1):
    return re.sub('(.)\x01+\\d+', '\x01', str1[56:-90])