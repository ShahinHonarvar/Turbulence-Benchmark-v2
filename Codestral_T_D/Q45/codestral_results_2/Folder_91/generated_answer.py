from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:7].lower()
    result = set()
    for i in range(3, len(s) + 1):
        perms = set(permutations(s, i))
        for p in perms:
            if p == p[::-1]:
                result.add(''.join(p))
    return result