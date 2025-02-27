from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    for p in permutations(string[5:10]):
        candidate = ''.join(p).lower()
        if len(candidate) >= 6 and candidate == candidate[::-1]:
            result.add(candidate)
    return result