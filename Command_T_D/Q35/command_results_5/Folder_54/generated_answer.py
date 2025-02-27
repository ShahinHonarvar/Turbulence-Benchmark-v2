import re

def remove_repeat_chars(s):
    return re.sub('((?<=35)[a-z])\x01(?!\x01(?<=64))', '', s)