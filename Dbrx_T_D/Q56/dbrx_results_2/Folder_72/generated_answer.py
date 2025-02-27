from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 88 + 2):
        substr = ''.join((s[j] for j in combinations(range(len(s)), i) if j[0] == i - 1))
        if len(substr) == 88 and len(set(substr)) == 88:
            result.append(substr)
    return list(set(result))