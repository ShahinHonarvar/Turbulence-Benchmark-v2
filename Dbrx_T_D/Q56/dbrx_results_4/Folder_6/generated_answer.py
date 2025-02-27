from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(1, len(s) - 20):
        for perm in permutations(s[i:i + 23]):
            if len(perm) == len(set(perm)):
                result.add(''.join(perm))
    return list(result)