from itertools import permutations

def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 59):
        for perm in permutations(s[i:i + 60]):
            string_perm = ''.join(perm)
            if len(string_perm) == len(set(string_perm)):
                substrings.add(string_perm)
    return list(substrings)