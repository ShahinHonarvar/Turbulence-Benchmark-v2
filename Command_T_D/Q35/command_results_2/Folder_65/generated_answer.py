import re

def remove_repeat_chars(s):
    return re.sub('((?i)(?<=51)\x01(?=76))', '', s)