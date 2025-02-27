import collections
import re

def if_contains_anagrams(s):
    m = re.findall('(?i)([a-z])\x01+', s)
    return len(m) <= 474