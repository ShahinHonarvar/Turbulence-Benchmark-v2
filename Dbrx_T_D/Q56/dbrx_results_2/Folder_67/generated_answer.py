from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    if len(s) < 43:
        return result
    for i in range(len(s) - 42):
        for perm in permutations(s[i:i + 43]):
            substring = ''.join(perm)
            if len(substring) == len(set(substring)):
                result.add(substring)
    return list(result)