from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    s = string[4:10].lower()
    for i in range(6, len(s) + 1):
        for p in permutations(s, i):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result