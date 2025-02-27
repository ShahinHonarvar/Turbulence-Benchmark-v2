from itertools import combinations

def all_substring_of_size_n(s):
    result = set()
    n = 41
    if len(s) < n:
        return []
    for i in range(len(s) - n + 1):
        substr = ''.join((s[j] for j in combinations(range(len(s)), n) if j[0] == i))
        if len(set(substr)) == n:
            result.add(substr)
    return list(result)