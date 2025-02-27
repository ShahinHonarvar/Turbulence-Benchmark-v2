from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    for p in permutations(string[2:7]):
        candidate = ''.join(p)
        if len(candidate) >= 5 and candidate.lower() == candidate[::-1].lower():
            result.add(candidate.lower())
    return result