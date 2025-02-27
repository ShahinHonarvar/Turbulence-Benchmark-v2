from itertools import permutations

def palindromes_between_indices(s):
    s = s[:4].lower()
    result = set()
    for i in range(4, len(s) + 1):
        for perm in permutations(s, i):
            if perm == perm[::-1]:
                result.add(''.join(perm))
    return result