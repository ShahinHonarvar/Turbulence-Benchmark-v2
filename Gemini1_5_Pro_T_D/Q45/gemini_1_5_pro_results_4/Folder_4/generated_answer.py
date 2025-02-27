from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join((c for c in string[3:10] if c.isalpha())).lower()
    if len(letters) < 7:
        return set()
    palindromes = set()
    for perm in {''.join(p) for p in permutations(letters)}:
        if len(perm) >= 7 and perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes