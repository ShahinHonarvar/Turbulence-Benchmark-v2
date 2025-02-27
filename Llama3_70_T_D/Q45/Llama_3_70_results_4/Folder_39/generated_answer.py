from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:6].lower()
    english_letters = [c for c in s if c.isalpha()]
    result = set()
    for r in range(3, len(english_letters) + 1):
        for p in permutations(english_letters, r):
            if p == p[::-1]:
                result.add(''.join(p))
    return result