from itertools import permutations

def palindromes_between_indices(s):
    substr = s[4:6].lower()
    result = set()
    for r in range(3, len(substr) + 1):
        for perm in permutations(substr, r):
            word = ''.join(perm)
            if word == word[::-1]:
                result.add(word)
    return result