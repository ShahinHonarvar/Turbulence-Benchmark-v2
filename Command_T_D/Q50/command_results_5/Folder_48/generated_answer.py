import re

def if_contains_anagrams(s):
    return bool(re.findall('(?i)(?=([a-z]))([a-z]{%d})\x01{%d}'.format(3, len(s) - 1), s))