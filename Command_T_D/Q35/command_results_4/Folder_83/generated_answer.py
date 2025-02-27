import re

def remove_repeat_chars(s):
    return re.sub('(.)\x01*(?:[a-z0-9])', '\x01\x02', s[100:-200])