from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[3:6] if c.isalpha()]
    letters = [c.lower() for c in letters]
    letters = list(set(letters))
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for p in permutations(letters, r):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes