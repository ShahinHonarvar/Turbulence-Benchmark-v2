from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[5:9] if c.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for p in permutations(letters, r):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes