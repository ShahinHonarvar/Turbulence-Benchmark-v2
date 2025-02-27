from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters = [c for c in s[1:6] if c.isalpha()]
    if len(letters) < 5:
        return set()
    result = set()
    for p in permutations(letters, 5):
        word = ''.join(p)
        if word == word[::-1]:
            result.add(word)
    return result