from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    s = s[0:6]
    pals = set()
    for i in range(3, len(s) + 1):
        perms = set(permutations(s, i))
        for perm in perms:
            word = ''.join(perm)
            if word == word[::-1]:
                pals.add(word)
    return pals