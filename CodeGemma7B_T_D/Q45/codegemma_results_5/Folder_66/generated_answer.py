from itertools import permutations

def palindromes_between_indices(text):
    result = set()
    for perm in permutations(text[0:6]):
        word = ''.join(perm)
        if word == word[::-1]:
            result.add(word.lower())
    return result