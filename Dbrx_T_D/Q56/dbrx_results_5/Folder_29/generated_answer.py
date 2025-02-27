from itertools import combinations

def all_substring_of_size_n(s):
    if len(s) < 95:
        return []
    result = []
    for comb in combinations(range(len(s)), 95):
        substr = ''.join((s[i] for i in comb))
        if len(substr) == len(set(substr)):
            result.append(substr)
    return list(set(result))