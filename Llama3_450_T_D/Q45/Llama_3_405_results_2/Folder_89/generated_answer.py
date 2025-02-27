import itertools

def palindromes_between_indices(s):
    english_letters = [c for c in s[5:10].lower() if c.isalpha()]
    if len(english_letters) < 6:
        return set()
    palindromes = set()
    for r in range(6, len(english_letters) + 1):
        for perm in itertools.permutations(english_letters, r):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes