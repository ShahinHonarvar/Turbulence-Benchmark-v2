from itertools import permutations
import re

def palindromes_between_indices(text):
    words = text[4:9].lower().split()
    if not words or len(max(words, key=len)) < 6:
        return set()
    letters = ''.join(re.findall('[a-zA-Z]', ''.join(words)))
    perms = set()
    for p in permutations(letters):
        p = ''.join(p)
        if len(p) >= 6 and p == p[::-1]:
            perms.add(p)
    return perms