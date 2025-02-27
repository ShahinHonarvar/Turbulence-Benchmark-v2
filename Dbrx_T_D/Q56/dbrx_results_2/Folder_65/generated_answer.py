from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for perm in permutations(s, 81):
        sub = ''.join(perm)
        if len(sub) == 81 and len(set(sub)) == 81:
            result.add(sub)
    return list(result)