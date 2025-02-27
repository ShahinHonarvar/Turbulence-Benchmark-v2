import re

def palindromes_between_indices(s):
    return set(re.findall('[a-z]+', s[5:7] + s[5:7][::-1]))