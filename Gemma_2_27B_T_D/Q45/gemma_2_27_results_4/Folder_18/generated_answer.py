from itertools import permutations

def palindromes_between_indices(s):
    letters = s[1:7].lower()
    pals = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 3:
            pals.add(word)
    return pals