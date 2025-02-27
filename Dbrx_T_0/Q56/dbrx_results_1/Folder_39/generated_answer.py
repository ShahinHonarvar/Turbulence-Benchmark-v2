from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 94 + 1):
        for perm in permutations(s[i:i + 94]):
            substring = ''.join(perm)
            if len(substring) == len(set(substring)):
                result.add(substring)
    return list(result)