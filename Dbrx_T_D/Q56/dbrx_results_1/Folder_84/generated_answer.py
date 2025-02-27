from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for perm in permutations(s, 114):
        sub = ''.join(perm)
        if len(sub) == 114 and len(set(sub)) == 114:
            result.add(sub)
    return list(result)