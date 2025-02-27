from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    if len(s) < 43:
        return []
    for i in range(len(s) - 42):
        substr = ''.join((s[j] for j in combinations(range(len(s)), 43)[i]))
        if len(set(substr)) == 43:
            result.append(substr)
    return list(set(result))