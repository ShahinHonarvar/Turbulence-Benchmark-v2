import re

def palindromes_between_indices(s):
    return set(re.findall('[a-z]+', s[4:-4]))