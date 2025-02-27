from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:10].lower()
    letters = [c for c in s if c.isalpha()]
    if len(letters) < 3:
        return set()
    pals = set()
    for r in range(6, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1]:
                pals.add(word)
    return pals