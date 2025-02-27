from itertools import permutations

def palindromes_between_indices(s):
    result = set()
    for p in permutations(s[0:8], r=4):
        word = ''.join(p).lower()
        if word == word[::-1]:
            result.add(word)
    return result