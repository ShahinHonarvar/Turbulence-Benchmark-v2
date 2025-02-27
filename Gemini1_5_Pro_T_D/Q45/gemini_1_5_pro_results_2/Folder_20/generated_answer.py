from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    for p in permutations(string[2:9]):
        s = ''.join(p).lower()
        if len(s) >= 4 and s == s[::-1]:
            result.add(s)
    return result