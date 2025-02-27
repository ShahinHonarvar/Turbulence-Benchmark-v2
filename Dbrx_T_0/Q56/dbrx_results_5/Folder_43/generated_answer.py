from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    if len(s) < 86:
        return result
    for perm in permutations(s, 86):
        substring = ''.join(perm)
        if len(substring) == len(set(substring)):
            result.append(substring)
    return list(set(result))