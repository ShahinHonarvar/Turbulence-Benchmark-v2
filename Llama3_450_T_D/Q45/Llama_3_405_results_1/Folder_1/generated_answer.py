import itertools

def palindromes_between_indices(s):
    s = s[4:8]
    s = ''.join(filter(str.isalpha, s)).lower()
    if len(s) < 5:
        return set()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for perm in itertools.permutations(letters, r):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes