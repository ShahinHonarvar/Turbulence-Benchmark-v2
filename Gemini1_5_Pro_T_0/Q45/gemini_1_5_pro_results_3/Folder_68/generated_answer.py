from itertools import permutations
  from collections import Counter

def palindromes_between_indices(string):
    letters = ''.join((c for c in string[1:9] if c.isalpha())).lower()
    result = set()
    for i in range(4, len(letters) + 1):
        for p in set(permutations(letters, i)):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result