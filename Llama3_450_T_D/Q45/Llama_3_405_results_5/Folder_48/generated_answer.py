from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[6:9] if c.isalpha()]
    letters = ''.join(letters).lower()
    palindromes = set()
    for r in range(len(letters)):
        for perm in permutations(letters, r + 1):
            p = ''.join(perm)
            if len(p) >= 4 and p == p[::-1]:
                palindromes.add(p)
    return palindromes