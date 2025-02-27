from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 92):
        for perm in permutations(s[i:i + 93]):
            t = ''.join(perm)
            if len(t) == 93 and len(set(t)) == 93:
                result.add(t)
    return list(result)