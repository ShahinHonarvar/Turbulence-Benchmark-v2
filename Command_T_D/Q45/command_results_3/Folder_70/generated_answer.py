import re

def palindromes_between_indices(s):
    return set(re.findall('[a-z]+', s[1:6:2][::-1]))