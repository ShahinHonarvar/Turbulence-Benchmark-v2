from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 95):
        substr = ''.join((s[j] for j in combinations(range(len(s)), i) if s[j] not in s[j + 1:]))
        if len(substr) == 96:
            result.append(substr)
    return list(set(result))