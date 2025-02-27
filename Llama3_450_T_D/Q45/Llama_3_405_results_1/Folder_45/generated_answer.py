from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:10] if c.isalpha()]
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for perm in permutations(letters, r):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes