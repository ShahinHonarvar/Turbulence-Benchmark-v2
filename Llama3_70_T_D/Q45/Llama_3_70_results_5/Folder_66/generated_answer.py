from itertools import combinations, permutations
import string

def palindromes_between_indices(s):
    s = s[:6].lower()
    s = ''.join((c for c in s if c in string.ascii_lowercase))
    pals = set()
    for r in range(5, len(s) + 1):
        for combo in combinations(s, r):
            for perm in permutations(combo):
                word = ''.join(perm)
                if word == word[::-1]:
                    pals.add(word)
    return pals