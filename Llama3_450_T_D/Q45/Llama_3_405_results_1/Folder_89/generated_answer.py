import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[5:10] if c.isalpha()]
    if len(letters) < 6:
        return set()
    letters = [c.lower() for c in letters]
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for perm in itertools.permutations(letters, r):
            if ''.join(perm) == ''.join(perm[::-1]):
                palindromes.add(''.join(perm))
    return palindromes