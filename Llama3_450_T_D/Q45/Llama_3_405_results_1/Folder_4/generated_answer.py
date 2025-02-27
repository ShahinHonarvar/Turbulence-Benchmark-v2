import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[3:10] if c.isalpha()]
    letters = ''.join(letters).lower()
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for p in itertools.permutations(letters, r):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes