from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    s = string[1:7]
    for i in range(4, len(s) + 1):
        for p in permutations(s, i):
            if ''.join(p).lower() == ''.join(reversed(''.join(p))).lower():
                result.add(''.join(p).lower())
    return result