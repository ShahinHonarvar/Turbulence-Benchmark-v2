from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join((c for c in string[3:10] if c.isalpha())).lower()
    result = set()
    if len(letters) < 5:
        return result
    for i in range(5, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result