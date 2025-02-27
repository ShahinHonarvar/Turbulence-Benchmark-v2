from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:8].lower()
    s = ''.join(filter(str.isalpha, s))
    pals = set()
    for r in range(4, len(s) + 1):
        for perm in permutations(s, r):
            word = ''.join(perm)
            if word == word[::-1]:
                pals.add(word)
    return pals