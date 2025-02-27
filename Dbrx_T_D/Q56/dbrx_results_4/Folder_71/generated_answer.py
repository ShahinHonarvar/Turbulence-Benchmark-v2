from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 16):
        perms = {''.join(p) for p in permutations(s[i:i + 17], 17)}
        result.update(perms)
    return list(result)