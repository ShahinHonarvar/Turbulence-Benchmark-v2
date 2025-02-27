from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    s = string[0:7]
    letters = ''.join((c for c in s if c.isalpha())).lower()
    if len(letters) < 5:
        return result
    for i in range(5, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result