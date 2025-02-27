from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for n in range(1, 80):
        for perm in permutations(s, n):
            substring = ''.join(perm)
            if len(substring) == n and len(substring) == len(set(substring)):
                result.add(substring)
    return list(result)