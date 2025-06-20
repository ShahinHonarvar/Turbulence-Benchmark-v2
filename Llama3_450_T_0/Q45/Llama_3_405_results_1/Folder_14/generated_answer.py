import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[4:6] if c.isalpha()]
    letters = [c.lower() for c in letters]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in itertools.permutations(letters, r):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes