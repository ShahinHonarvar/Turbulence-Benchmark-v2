from collections import Counter
  from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[:8] if c.isalpha())).lower()
    if len(letters) < 6:
        return set()
    palindromes = set()
    for i in range(6, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes