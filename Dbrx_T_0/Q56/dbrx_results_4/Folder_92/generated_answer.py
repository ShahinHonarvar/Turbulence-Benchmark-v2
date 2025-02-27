from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 8):
        for perm in permutations(s[i:i + 9]):
            t = ''.join(perm)
            if len(t) == 9 and len(set(t)) == 9:
                result.add(t)
    return list(result)