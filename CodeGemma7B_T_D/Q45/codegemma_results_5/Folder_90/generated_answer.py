from itertools import permutations

def palindromes_between_indices(txt):
    low_txt = txt.lower()
    letters = [c for c in low_txt[0:6] if c.isalpha()]
    res = []
    for letters in permutations(letters):
        word = ''.join(letters)
        if word == word[::-1]:
            res.append(word)
    return set(res)