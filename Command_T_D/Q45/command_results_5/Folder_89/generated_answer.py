import re

def palindromes_between_indices(s):
    return set(re.findall('<(.)>(.)<\x01>', s[5:-4:-1]) + re.findall('<(.)>(.)<\x02>', s[5:-4:-1]))