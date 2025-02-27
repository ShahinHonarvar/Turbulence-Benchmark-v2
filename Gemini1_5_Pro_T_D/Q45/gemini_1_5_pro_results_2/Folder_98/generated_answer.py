from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join((c for c in string[3:6] if c.isalpha())).lower()
    if len(letters) < 4:
        return set()
    palindromes = set()
    for perm in {''.join(p) for i in range(4, len(letters) + 1) for p in permutations(letters, i)}:
        if perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes