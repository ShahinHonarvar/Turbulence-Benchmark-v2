from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:8].lower()
    letters = [c for c in s if c.isalpha()]
    if len(letters) < 2:
        return set()
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for p in permutations(letters, r):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes