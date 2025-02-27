import re

def remove_repeat_chars(str1):
    return re.sub('(.)\x01(.)', '\x01\x02', str1[35:-65])