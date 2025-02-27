from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(1, 99):
        for perm in permutations(s, i):
            sub = ''.join(perm)
            if len(sub) == 98 and len(set(sub)) == 98:
                result.add(sub)
    return list(result)