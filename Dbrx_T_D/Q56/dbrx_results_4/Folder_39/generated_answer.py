from itertools import combinations

def all_substring_of_size_n(s):
    substrings = []
    n = 94
    if n > len(s):
        return []
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) == n and len(set(substring)) == n:
            substrings.append(substring)
    return list(set(substrings))