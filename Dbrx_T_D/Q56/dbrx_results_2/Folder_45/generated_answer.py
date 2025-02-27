from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for perm in permutations(s, 29):
        sub = ''.join(perm)
        if len(sub) == len(set(sub)):
            result.add(sub)
    return list(result)