import re

def palindromes_between_indices(s):
    s = re.sub('([A-Z])', ' \x01', s)
    return set(re.findall('(.)\x01\x02\x03\x04\x05', s))