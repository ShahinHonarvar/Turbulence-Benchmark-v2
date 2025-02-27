from collections import Counter
from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:8].lower()
    letters = [c for c in s if c.isalpha()]
    counter = Counter(letters)
    result = set()
    for r in range(4, len(s) + 1):
        for p in permutations(letters, r):
            if p == p[::-1]:
                word = ''.join(p)
                counter_copy = counter.copy()
                for c in word:
                    if c not in counter_copy or counter_copy[c] == 0:
                        break
                    counter_copy[c] -= 1
                else:
                    result.add(word)
    return result