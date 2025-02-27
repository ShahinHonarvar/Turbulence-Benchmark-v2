from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:6] if c.isalpha()]
    if len(letters) < 5:
        return set()
    result = set()
    for r in range(5, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result