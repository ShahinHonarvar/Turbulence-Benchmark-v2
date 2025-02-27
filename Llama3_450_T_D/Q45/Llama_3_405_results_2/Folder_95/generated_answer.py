import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[7:9] if c.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for p in itertools.permutations(letters, r):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes