import re

def remove_repeat_chars(s):
    return re.sub('(\\D)(?=\x01(?!\x01)),', '', s, flags=re.I)