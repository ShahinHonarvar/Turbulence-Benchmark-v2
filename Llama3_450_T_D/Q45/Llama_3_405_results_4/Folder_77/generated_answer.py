from itertools import permutations

def palindromes_between_indices(s):
    english_letters = [c for c in s[4:7] if c.isalpha()]
    palindromes = set()
    for r in range(4, len(english_letters) + 1):
        for p in permutations(english_letters, r):
            if ''.join(p).lower() == ''.join(reversed(p)).lower():
                palindromes.add(''.join(p).lower())
    return palindromes