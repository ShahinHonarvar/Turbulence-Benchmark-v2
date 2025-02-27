import re

def palindromes_of_specific_lengths(s):
    match = re.findall('[a-z]{41}([a-z]+){38}([a-z]{41})', s.lower())
    return set((m[0] for m in match if len(m[1]) in range(23, 39)))