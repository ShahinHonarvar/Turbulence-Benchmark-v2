from itertools import permutations

def palindromes_between_indices(s):
    english_letters = [c.lower() for c in s[1:7] if c.isalpha()]
    palindromes = set()
    for r in range(6, len(english_letters) + 1):
        for perm in permutations(english_letters, r):
            p = ''.join(perm)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes