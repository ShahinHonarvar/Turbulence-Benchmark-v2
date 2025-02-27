from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:8] if c.isalpha()]
    sets = set()
    for r in range(4, len(letters) + 1):
        for t in set(permutations(letters, r)):
            word = ''.join(t)
            if word == word[::-1]:
                sets.add(word)
    return sets