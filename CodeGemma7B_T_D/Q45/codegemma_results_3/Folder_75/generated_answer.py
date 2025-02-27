from itertools import permutations

def palindromes_between_indices(text):
    perms = permutations(text[2:5], 3)
    result = set()
    for perm in perms:
        word = ''.join(perm).lower()
        if word == word[::-1]:
            result.add(word)
    return result