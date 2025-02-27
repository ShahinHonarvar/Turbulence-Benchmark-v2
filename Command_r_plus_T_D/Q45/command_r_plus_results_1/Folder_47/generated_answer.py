import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[3:8])
    permutations = set()
    for l in letters:
        permutations.add(l.lower())
        permutations.add(l.upper())
    palindromes = set((p for p in permutations if p == p[::-1] and len(p) >= 5))
    return palindromes