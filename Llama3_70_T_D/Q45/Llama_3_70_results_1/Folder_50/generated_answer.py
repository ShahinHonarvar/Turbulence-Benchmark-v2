from collections import Counter
from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters = ''.join(filter(str.isalpha, s[4:9]))
    counter = Counter(letters)
    result = set()
    for r in range(5, len(letters) + 1):
        for perm in permutations(letters, r):
            word = ''.join(perm)
            if word == word[::-1]:
                mid = len(word) // 2
                is_valid = True
                for c in word[:mid]:
                    if counter[c] == 0:
                        is_valid = False
                        break
                    counter[c] -= 1
                if is_valid:
                    result.add(word)
                for c in word[:mid]:
                    counter[c] += 1
    return result