import re

def remove_repeat_chars(s):
    return re.sub('((?i)[a-z]{50,92})\x01+', '\x01', s)