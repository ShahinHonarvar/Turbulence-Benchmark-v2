from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[3:6] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    for r in range(2, len(letters) + 1):
        for perm in permutations(letters, r):
            p = ''.join(perm)
            if p == p[::-1] and len(p) >= 4:
                palindromes.add(p)
    return palindromes