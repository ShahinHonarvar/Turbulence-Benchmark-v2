from itertools import permutations as perm

def palindromes_between_indices(text):
    text = text[4:7].lower()
    if text.isalpha():
        return set((''.join(p) for p in perm(text)))
    return set()