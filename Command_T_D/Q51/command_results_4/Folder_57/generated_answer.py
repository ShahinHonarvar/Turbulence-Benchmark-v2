import collections
import re

def if_contains_anagrams(s):
    return bool(re.findall('[a-z]', collections.Counter(s).keys()))