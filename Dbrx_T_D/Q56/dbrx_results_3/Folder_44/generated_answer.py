from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for n in range(1, min(91, len(s)) + 1):
        for perm in permutations(s, n):
            t = ''.join(perm)
            if len(t) == len(set(t)):
                result.add(t)
    return list(result)