from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(1, min(39, len(s) + 1)):
        for perm in permutations(s, i):
            substring = ''.join(perm)
            if len(substring) == 38 and len(set(substring)) == 38:
                result.add(substring)
    return list(result)