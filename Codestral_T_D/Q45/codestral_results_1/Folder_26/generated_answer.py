from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:7].lower()
    result = set()
    for i in range(3, len(s) + 1):
        perms = permutations(s, i)
        for p in perms:
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result