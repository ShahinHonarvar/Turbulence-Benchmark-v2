import re

def remove_repeat_chars(s):
    return re.sub('((?<=13)[a-z]+(?<=76))\x01', '', s)