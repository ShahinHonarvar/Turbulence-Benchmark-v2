import re

def remove_repeat_chars(s):
    return re.sub('((?=.)\x01+)(\\d+)', '\x01\x02', s[13:-70])