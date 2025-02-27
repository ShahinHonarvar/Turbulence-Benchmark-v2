from itertools import combinations

def all_substring_of_size_n(s):
    n = 63
    substrings = []
    if len(s) < n:
        return []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n:
            substrings.append(substring)
    return list(set(substrings))