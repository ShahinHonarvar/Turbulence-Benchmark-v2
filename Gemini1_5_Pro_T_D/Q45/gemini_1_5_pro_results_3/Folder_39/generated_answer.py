from itertools import permutations
  from collections import Counter

def palindromes_between_indices(string):
    letters = ''.join((c for c in string[2:6] if c.isalpha())).lower()
    result = set()
    for i in range(3, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result