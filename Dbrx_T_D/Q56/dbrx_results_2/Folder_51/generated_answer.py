from itertools import combinations

def all_substring_of_size_n(s):
    n = 96
    substrings = []
    if len(s) < n:
        return []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            substrings.append(substring)
        elif len(set(substring)) < n:
            continue
    return list(set(substrings))