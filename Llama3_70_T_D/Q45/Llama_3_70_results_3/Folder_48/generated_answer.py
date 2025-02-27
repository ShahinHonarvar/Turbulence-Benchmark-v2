import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[6:9] if c.isalpha()]
    if len(letters) == 0:
        return set()
    palindromes = set()
    for r in range(4, len(letters) + 1):
        for perm in itertools.permutations(letters, r):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes