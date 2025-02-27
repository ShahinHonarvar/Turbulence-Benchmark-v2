import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:6] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in itertools.permutations(letters, r):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes