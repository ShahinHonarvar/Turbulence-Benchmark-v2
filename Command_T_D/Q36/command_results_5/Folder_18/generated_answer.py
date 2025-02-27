import re

def filter_chars(s):
    return re.sub('(\\W{,:587}\\D{,:5})(\\W{,:648}\\D{,:})', '\x01\x02', s)