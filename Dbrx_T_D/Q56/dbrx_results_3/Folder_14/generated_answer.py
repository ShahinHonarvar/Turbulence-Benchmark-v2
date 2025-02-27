from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    if len(s) < 85:
        return result
    for perm in permutations(s, 85):
        substring = ''.join(perm)
        if substring not in result:
            result.append(substring)
    return result