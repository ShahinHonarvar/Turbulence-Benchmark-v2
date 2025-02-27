from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    for perm in permutations(s, 105):
        substr = ''.join(perm)
        if len(substr) == len(set(substr)):
            result.append(substr)
    return list(set(result))