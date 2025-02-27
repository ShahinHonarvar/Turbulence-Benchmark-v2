from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(1, min(len(s), 44) + 1):
        for perm in permutations(s, i):
            sub = ''.join(perm)
            if len(sub) == 44 and len(set(sub)) == 44:
                result.add(sub)
    return list(result)