import re

def remove_repeat_chars(str):
    return re.sub('(.)\x01+', '\x01', str[17:-88])