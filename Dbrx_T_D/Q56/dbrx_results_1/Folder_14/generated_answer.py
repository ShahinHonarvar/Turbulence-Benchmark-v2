from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 84):
        perms = {''.join(p) for p in permutations(s[i:i + 85], 85)}
        result.update(perms)
    return list(result)