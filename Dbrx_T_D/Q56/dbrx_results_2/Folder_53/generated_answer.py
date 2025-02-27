from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 24):
        substr = ''.join((s[j] for j in combinations(range(len(s)), i) if all((s[j] != s[k] for j, k in combinations(range(i), 2)))))
        if len(substr) == 25:
            result.append(substr)
    return list(set(result))