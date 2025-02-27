import re

def remove_repeat_chars(s):
    return re.sub('((?<=36)(?=85))\x01+', '', s)