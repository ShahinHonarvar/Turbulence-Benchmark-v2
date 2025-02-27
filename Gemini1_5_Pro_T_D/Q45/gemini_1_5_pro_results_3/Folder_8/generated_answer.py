from itertools import permutations
    from collections import Counter

def palindromes_between_indices(string):
    letters = ''.join((c for c in string[1:6] if c.isalpha()))
    result = set()
    for i in range(5, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p).lower()
            if word == word[::-1] and word not in result:
                result.add(word)
    return result