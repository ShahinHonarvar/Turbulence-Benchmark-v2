from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:8].lower()
    result = set()
    for i in range(6, len(s) + 1):
        perms = set(permutations(s, i))
        for perm in perms:
            word = ''.join(perm)
            if word == word[::-1]:
                result.add(word)
    return result