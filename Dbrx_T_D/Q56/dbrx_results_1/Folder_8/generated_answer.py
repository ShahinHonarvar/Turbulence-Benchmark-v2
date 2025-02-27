from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    if len(s) < 30:
        return result
    for i in range(len(s) - 29):
        substr = ''.join((s[j] for j in combinations(range(len(s)), 30)[i]))
        if len(set(substr)) == 30:
            result.append(substr)
    return list(set(result))