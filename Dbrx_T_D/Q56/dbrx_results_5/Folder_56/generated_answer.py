from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 68):
        for perm in permutations(s[i:i + 69]):
            t = ''.join(perm)
            if len(t) == 69 and len(set(t)) == 69:
                result.add(t)
    return list(result)