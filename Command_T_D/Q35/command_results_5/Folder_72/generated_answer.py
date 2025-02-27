import re

def remove_repeat_chars(str1):
    return re.sub('([a-z]{13})([a-z]{70})([a-z]{13})', '\x01\x02', str1)