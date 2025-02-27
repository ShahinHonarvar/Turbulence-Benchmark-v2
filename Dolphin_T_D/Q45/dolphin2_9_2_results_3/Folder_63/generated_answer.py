from itertools import permutations

def palindromes_between_indices(s):
    s = s[:4].lower()
    result = set()
    for p in permutations(s, 3):
        word = ''.join(p)
        if word == word[::-1]:
            result.add(word)
    return result