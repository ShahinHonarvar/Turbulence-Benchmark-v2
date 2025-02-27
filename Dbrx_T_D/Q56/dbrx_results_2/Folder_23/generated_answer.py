from itertools import combinations

def all_substring_of_size_n(s):
    n = 42
    if len(s) < n or len(set(s)) < n:
        return []
    substrings = []
    for combo in combinations(range(len(s)), n):
        substr = s[combo[0]:combo[0] + n]
        if len(substr) == len(set(substr)):
            substrings.append(substr)
    return list(set(substrings))