from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 55 + 2):
        substrings = [''.join(substr) for substr in combinations(s[i - 1:i + 54], 55)]
        result.extend(substrings)
    return list(set(result))