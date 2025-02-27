from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    s = string[5:10].lower()
    for i in range(len(s) + 1):
        for p in permutations(s):
            candidate = ''.join(p)
            if len(candidate) >= 6 and candidate == candidate[::-1]:
                result.add(candidate)
    return result