from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[1:3] if c.isalpha()]
    pals = set()
    for p in permutations(letters, len(letters)):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 3:
            pals.add(word.lower())
    return pals