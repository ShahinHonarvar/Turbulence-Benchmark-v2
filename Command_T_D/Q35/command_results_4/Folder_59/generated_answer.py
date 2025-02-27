import re

def remove_repeat_chars(s):
    return re.sub('((?=([^aieou]))\x01+)', '\x01', s)