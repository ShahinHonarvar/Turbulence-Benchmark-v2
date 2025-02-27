from itertools import permutations
  from collections import Counter

def palindromes_between_indices(string):
    letters = ''.join((char for char in string[0:6] if char.isalpha())).lower()
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for p in permutations(letters, i):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                palindromes.add(candidate)
    return palindromes