from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters = [c for c in s[1:9] if c.isalpha()]
    seen = set()
    for p in permutations(letters, 7):
        word = ''.join(p)
        if word == word[::-1] and word not in seen:
            seen.add(word)
    return seen