import itertools

def palindromes_between_indices(s):
    s = s[8:10]
    letters = [c for c in s if c.isalpha()]
    letters = ''.join(letters).lower()
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for p in itertools.permutations(letters, r):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes