import re

def palindromes_between_indices(s):
    m = re.findall('[A-Za-z]+', s[2:-2])
    return {i.lower() for i in m if i[::-1] == i}