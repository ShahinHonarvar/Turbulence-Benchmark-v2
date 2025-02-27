from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[:9] if c.isalpha())).lower()
    palindromes = set()
    for r in range(7, len(letters) + 1):
        for p in permutations(letters, r):
            if ''.join(p) == ''.join(p)[::-1]:
                palindromes.add(''.join(p))
    return palindromes