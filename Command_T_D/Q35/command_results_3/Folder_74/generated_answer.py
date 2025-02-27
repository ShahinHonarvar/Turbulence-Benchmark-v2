import re

def remove_repeat_chars(s):
    return re.sub('((?<=\\d)\\w)\x01+', '', s)