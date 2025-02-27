import re

def palindromes_between_indices(s):
    return set(re.findall('([a-z]+)(?=\x08[a-z]{5}\x08[a-z]+)', s[2:-2]))