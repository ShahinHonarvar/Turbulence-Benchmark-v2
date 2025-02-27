from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 60 + 1):
        perm = (''.join(p) for p in permutations(s[i:i + 60]))
        result.update(filter(lambda x: len(set(x)) == len(x), perm))
    return list(result)