from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:10].lower()
    s = ''.join(filter(str.isalpha, s))
    pals = set()
    for r in range(4, len(s) + 1):
        for perm in permutations(s, r):
            ss = ''.join(perm)
            if ss == ss[::-1]:
                pals.add(ss)
    return pals