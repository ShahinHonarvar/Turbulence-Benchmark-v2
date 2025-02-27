import re

def remove_repeat_chars(str1):
    str1 = str(str1)[57:-85]
    return re.sub('([a-z])\x01+', '\x01', str1)