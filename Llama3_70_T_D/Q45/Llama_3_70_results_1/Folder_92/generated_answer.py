from itertools import permutations

def palindromes_between_indices(s):
    letters = set((c.lower() for c in s[4:8] if c.isalpha()))
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for p in permutations(letters, r):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes