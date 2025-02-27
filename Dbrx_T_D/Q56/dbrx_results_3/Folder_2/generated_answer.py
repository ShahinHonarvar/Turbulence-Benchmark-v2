from itertools import combinations

def all_substring_of_size_n(s):
    n = 56
    substrings = []
    for comb in combinations(range(len(s)), n):
        if len(set((s[i] for i in comb))) == n:
            substrings.append(''.join((s[i] for i in comb)))
    return list(set(substrings))