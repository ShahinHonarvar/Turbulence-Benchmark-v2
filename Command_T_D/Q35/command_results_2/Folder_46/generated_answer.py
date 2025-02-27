import re

def remove_repeat_chars(str1):
    return re.sub('((?i)(\\d)(?=\\d\x01)', '\x01', str1[10:79])