from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for n in range(1, len(s) + 1):
        for perm in permutations(s, n):
            t = ''.join(perm)
            if len(t) == 90 and len(set(t)) == 90:
                result.add(t)
    return list(result)