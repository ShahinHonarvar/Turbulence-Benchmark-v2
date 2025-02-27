from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(49, 0, -1):
        for perm in permutations(s, i):
            substring = ''.join(perm)
            if len(substring) == 49 and len(set(substring)) == 49:
                result.add(substring)
    return list(result)