import re

def remove_repeat_chars(s):
    return re.sub('(.)\x01+([^a-z]{50,92})', '\x01\x02', s)