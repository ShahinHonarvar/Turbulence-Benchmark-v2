from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:10].lower()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    s = ''.join((c for c in s if c in english_letters))
    result = set()
    for r in range(6, len(s) + 1):
        for p in permutations(s, r):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result