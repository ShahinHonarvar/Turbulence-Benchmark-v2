from itertools import permutations

def palindromes_between_indices(s):
    s = ''.join((c for c in s if c.isalpha())).lower()
    if len(s) < 7:
        return set()
    substrings = set()
    for p in permutations(s[:7], 4):
        substrings.add(''.join(p))
    palindromes = set()
    for sub in substrings:
        if sub == sub[::-1]:
            palindromes.add(sub)
    return palindromes