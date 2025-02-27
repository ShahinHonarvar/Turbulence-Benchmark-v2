from itertools import permutations
  from collections import Counter

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[1:7] if c.isalpha())).lower()
    result = set()
    for i in range(3, len(letters) + 1):
        for p in permutations(letters, i):
            if ''.join(p) == ''.join(p)[::-1]:
                result.add(''.join(p))
    return result