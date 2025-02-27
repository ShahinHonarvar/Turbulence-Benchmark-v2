from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:8].lower()
    result = set()
    for i in range(4, len(s) + 1):
        for p in permutations(s, i):
            p = ''.join(p)
            if p == p[::-1]:
                result.add(p)
    return result