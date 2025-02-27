from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 116):
        for perm in permutations(s[i:i + 117]):
            t = ''.join(perm)
            if len(t) == len(set(t)):
                result.add(t)
    return list(result)