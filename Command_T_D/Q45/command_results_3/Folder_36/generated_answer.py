import re

def palindromes_between_indices(s):
    return set(re.findall('(?i)(?P<1>[a-z])\x01(?P<2>[a-z])\x02(?P=1)(?P=2)', s[5:-8]))