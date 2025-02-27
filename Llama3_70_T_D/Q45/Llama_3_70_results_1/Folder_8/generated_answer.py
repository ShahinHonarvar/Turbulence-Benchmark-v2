from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:6] if c.isalpha()]
    result = set()
    for p in permutations(letters, 5):
        word = ''.join(p)
        if word == word[::-1]:
            result.add(word)
    return result