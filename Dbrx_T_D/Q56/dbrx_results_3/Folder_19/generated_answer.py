from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 17):
        for perm in permutations(s[i:i + 18]):
            t = ''.join(perm)
            if len(t) == 18 and len(set(t)) == 18:
                result.append(t)
    return list(set(result))