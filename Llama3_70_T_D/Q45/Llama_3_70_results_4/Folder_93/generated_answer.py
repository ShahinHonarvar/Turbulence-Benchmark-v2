import itertools

def palindromes_between_indices(s):
    s = s[2:8].lower()
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for r in range(6, len(letters) + 1):
        for p in itertools.permutations(letters, r):
            if p == p[::-1]:
                palindromes.add(''.join(p))
    return palindromes