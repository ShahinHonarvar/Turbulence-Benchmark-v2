from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    if len(s) < 79:
        return []
    for i in range(len(s) - 78):
        for perm in permutations(s[i:i + 79]):
            t = ''.join(perm)
            if len(t) == len(set(t)):
                result.add(t)
    return list(result)