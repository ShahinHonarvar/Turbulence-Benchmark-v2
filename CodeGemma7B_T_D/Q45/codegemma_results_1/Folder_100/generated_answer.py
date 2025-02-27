from itertools import permutations

def palindromes_between_indices(txt):
    WORDS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    res = set()
    for w in permutations(txt):
        if all((l in WORDS for l in w)) and len(w) >= 6:
            res.add(''.join(w))
    return res