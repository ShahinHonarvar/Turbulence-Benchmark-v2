from itertools import permutations
from collections import Counter

def palindromes_between_indices(s):
    letter_counter = Counter(s)
    letters = list(letter_counter.keys())
    n = len(letters)
    perms = set()
    for r in range(7, n + 1):
        for perm in permutations(letters, r):
            word = ''.join(perm)
            if word == word[::-1] and all((letter_counter[c] >= word.count(c) for c in perm)):
                perms.add(word[::-1])
    return perms