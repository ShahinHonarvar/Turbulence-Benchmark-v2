from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:10] if c.isalpha()]
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for p in permutations(letters, r):
            w = ''.join(p)
            if w == w[::-1]:
                palindromes.add(w)
    return palindromes