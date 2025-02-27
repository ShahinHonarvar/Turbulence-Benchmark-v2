from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    if len(s) < 86:
        return []
    for perm in permutations(s, 86):
        substring = ''.join(perm)
        if len(substring) == len(set(substring)):
            result.add(substring)
    return list(result)