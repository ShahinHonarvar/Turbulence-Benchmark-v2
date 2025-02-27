from itertools import combinations, permutations

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s if c.isalpha() and 1 <= s.index(c) <= 3))
    if len(letters) < 2:
        return set()
    palindromes = set()
    for comb in combinations(letters, 4):
        for perm in permutations(comb):
            letters = ''.join(perm)
            if letters == letters[::-1]:
                palindromes.add(letters)
    return palindromes