import re
  from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(sorted((c for c in string[1:9] if c.isalpha()))).lower()
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1] and word not in palindromes:
                palindromes.add(word)
    return palindromes