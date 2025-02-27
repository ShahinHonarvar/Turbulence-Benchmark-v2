from itertools import permutations

def palindromes_between_indices(s):
    s = s[:8].lower()
    letters = [c for c in s if c.isalpha()]
    pals = set()
    for p in permutations(letters, 7):
        word = ''.join(p)
        if word == word[::-1]:
            pals.add(word)
    return pals