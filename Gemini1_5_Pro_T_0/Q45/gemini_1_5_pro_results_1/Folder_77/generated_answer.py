from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    s = string[4:7].lower()
    for i in range(4, len(s) + 1):
        for p in permutations(s, i):
            candidate = ''.join(p)
            if candidate == candidate[::-1] and len(candidate) >= 4:
                result.add(candidate)
    return result