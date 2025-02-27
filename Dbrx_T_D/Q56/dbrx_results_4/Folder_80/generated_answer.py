from itertools import combinations

def all_substring_of_size_n(s):
    n = 31
    substrings = []
    if n > len(s) or len(set(s)) < n:
        return []
    for comb in combinations(range(len(s)), n):
        substring = ''.join((s[i] for i in comb))
        if len(set(substring)) == n:
            substrings.append(substring)
    return list(set(substrings))