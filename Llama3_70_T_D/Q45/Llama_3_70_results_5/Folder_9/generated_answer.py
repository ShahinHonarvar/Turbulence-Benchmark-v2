from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = [c for c in s if c.isalpha()]
    pals = set()
    for p in permutations(letters):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 7:
            pals.add(word)
    return pals