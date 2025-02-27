import re

def remove_repeat_chars(s):
    return re.sub('(.)\x01*(?:[0-9])', '\x01', s[100:-100])