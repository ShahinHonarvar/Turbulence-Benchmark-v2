from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:7].lower()
    letters = [c for c in s if c.isalpha()]
    result = set()
    for r in range(4, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result