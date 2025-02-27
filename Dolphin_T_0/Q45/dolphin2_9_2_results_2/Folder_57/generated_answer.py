from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    indices = s[2:6]
    pals = set()
    for p in permutations(indices):
        word = ''.join(p)
        if len(word) >= 5 and word == word[::-1]:
            pals.add(word)
    return pals