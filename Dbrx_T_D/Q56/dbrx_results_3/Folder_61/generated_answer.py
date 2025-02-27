from itertools import combinations

def all_substrings_of_size_n(s):
    n = 39
    substrings = []
    if len(s) < n:
        return []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) == len(set(substring)):
            substrings.append(substring)
    return list(set(substrings))