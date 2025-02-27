from itertools import permutations

def all_substring_of_size_n(s):
    n = 106
    substrings = set()
    for i in range(len(s) - n + 1):
        for perm in permutations(s[i:i + n]):
            substring = ''.join(perm)
            if len(substring) == len(set(substring)):
                substrings.add(substring)
    return list(substrings)