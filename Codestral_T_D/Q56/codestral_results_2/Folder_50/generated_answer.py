from itertools import combinations

def all_substring_of_size_n(s):
    n = 11
    return [''.join(sorted(set(s[i:j]))) for i, j in combinations(range(len(s) + 1), 2) if len(s[i:j]) == n and len(set(s[i:j])) == n]