from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:6].lower()
    result = set()
    for length in range(3, len(s) + 1):
        for perm in permutations(s, length):
            word = ''.join(perm)
            if word == word[::-1]:
                result.add(word)
    return result