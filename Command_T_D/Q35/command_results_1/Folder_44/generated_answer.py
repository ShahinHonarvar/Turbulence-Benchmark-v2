import re

def remove_repeat_chars(s):
    return re.sub('((?<=\\d)[a-z])\x01+', '', s[36:-52])