import re

def palindromes_between_indices(s):
    return set(re.findall('((?i)(?P<left>[a-z]+)\x01(?P<right>[a-z]+)\x02(?P=left))', s))