from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    for p in permutations(string[4:9]):
        s = ''.join(p)
        if len(s) >= 6 and s.lower() == s.lower()[::-1]:
            result.add(s.lower())
    return result