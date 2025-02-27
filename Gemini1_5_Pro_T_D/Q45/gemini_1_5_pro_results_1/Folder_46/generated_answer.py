from itertools import permutations
  from collections import Counter

def palindromes_between_indices(string):
    letters = ''.join((char for char in string[4:10] if char.isalpha())).lower()
    result = set()
    for i in range(6, len(letters) + 1):
        for p in permutations(letters, i):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result