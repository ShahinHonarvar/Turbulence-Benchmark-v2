import re

def palindromes_between_indices(s):
    indices = range(3, len(s) - 3)
    letters = ''.join(re.findall('[a-z]+', s[indices]))
    return set(re.findall('[a-z]+\x01[a-z]+', letters))