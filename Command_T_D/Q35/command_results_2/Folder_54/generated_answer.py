import re

def remove_repeat_chars(s):
    return re.sub('((?=.)\x01)', ' ', s[35:-65])