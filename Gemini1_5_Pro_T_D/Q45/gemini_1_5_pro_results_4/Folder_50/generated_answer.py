from itertools import permutations
    from collections import Counter

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[4:9] if c.isalpha())).lower()
    return {''.join(p) for i in range(5, len(letters) + 1) for p in permutations(letters, i) if ''.join(p) == ''.join(reversed(''.join(p))) and len(''.join(p)) >= 5}