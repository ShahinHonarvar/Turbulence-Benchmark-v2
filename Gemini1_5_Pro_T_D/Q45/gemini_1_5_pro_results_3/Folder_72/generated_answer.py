from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join((c for c in string[1:8] if c.isalpha())).lower()
    result = set()
    for i in range(6, len(letters) + 1):
        for j in permutations(letters, i):
            word = ''.join(j)
            if word == word[::-1]:
                result.add(word)
    return result