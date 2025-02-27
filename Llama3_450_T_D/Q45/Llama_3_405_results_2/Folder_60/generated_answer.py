from itertools import permutations

def palindromes_between_indices(s):
    english_letters = [c for c in s[3:7] if c.isalpha()]
    english_letters = [c.lower() for c in english_letters]
    palindromes = set()
    for r in range(4, len(english_letters) + 1):
        for perm in permutations(english_letters, r):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes