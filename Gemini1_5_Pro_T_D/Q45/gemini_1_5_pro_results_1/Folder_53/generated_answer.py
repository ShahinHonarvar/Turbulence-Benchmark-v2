from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    for p in permutations(string[4:9]):
        candidate = ''.join(p)
        if len(candidate) >= 6 and candidate.lower() == candidate[::-1].lower():
            result.add(candidate)
    return result