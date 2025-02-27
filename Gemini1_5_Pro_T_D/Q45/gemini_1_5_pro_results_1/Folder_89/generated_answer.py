from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join((c for c in string[5:10] if c.isalpha())).lower()
    length = len(letters)
    if length < 6:
        return set()
    palindromes = set()
    for perm in {''.join(p) for p in permutations(letters)}:
        if len(perm) >= 6 and perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes