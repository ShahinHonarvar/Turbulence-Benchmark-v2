from itertools import permutations

def palindromes_between_indices(s):
    pals = set()
    sub = s[1:5]
    for p in permutations(sub):
        word = ''.join(p)
        if len(word) >= 4 and word.lower() == word.lower()[::-1]:
            pals.add(word)
    return pals