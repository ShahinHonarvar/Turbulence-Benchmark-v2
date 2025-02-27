from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    for i in range(3, 7):
        for p in permutations(string[2:7], i):
            s = ''.join(p).lower()
            if s == s[::-1]:
                result.add(s)
    return result