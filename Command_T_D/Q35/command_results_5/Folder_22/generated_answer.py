import re

def remove_repeat_chars(str):
    return re.sub('(.)\x01+\x02', '\x01', str[50:-200])