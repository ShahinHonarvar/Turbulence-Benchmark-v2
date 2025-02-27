import re

def palindromes_between_indices(s):
    return set(re.findall('(?i)(?=((?P<a>[a-z])\x03+[a-z])))', s))