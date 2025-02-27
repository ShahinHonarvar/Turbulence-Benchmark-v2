from itertools import permutations, combinations

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s[:6]))
    result = set()
    for length in range(5, len(s) + 1):
        for t in combinations(s, length):
            if t == t[::-1]:
                result.add(t)
    return result