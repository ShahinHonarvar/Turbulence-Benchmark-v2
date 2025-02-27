import re

def remove_repeat_chars(str1):
    return re.sub('([a-z])\x01+', '\x01', str1[70:-98])