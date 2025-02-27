import re

def palindromes_between_indices(s):
    return re.findall('[a-z]+\\d+[a-z]+', s[4:-4])