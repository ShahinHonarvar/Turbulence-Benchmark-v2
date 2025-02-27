from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 8):
        for perm in permutations(s[i:i + 9]):
            sub = ''.join(perm)
            if len(sub) == len(set(sub)):
                result.add(sub)
    return list(result)