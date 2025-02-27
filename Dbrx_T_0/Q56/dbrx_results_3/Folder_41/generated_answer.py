from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 74 + 1):
        for perm in permutations(s[i:i + 74]):
            substring = ''.join(perm)
            if len(substring) == len(set(substring)):
                result.add(substring)
    return list(result)