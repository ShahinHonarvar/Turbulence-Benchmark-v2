import re

def remove_repeat_chars(s):
    return re.sub('((?<=<|(?<=\\d)))\x01', '', s, flags=re.I)