from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    substring = ''.join((c for c in s[2:5] if c.isalpha())).lower()
    result = set()
    for i in range(4, len(substring) + 1):
        for perm in permutations(substring, i):
            if perm == perm[::-1]:
                result.add(''.join(perm))
    return result