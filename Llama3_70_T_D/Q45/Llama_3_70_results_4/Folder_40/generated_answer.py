from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters = [c for c in s[4:10] if c.isalpha()]
    letters_set = set(letters)
    result = set()
    for r in range(7, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(''.join(p))
    return result