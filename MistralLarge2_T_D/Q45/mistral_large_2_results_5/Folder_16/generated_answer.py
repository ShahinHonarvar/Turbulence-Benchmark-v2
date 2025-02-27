from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[6:10] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for p in permutations(letters, r):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes