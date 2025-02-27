import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:10] if c.isalpha()]
    if len(letters) < 6:
        return set()
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for permutation in itertools.permutations(letters, r):
            p = ''.join(permutation)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes