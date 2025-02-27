from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    if len(s) < 93:
        return result
    for i in range(len(s) - 92):
        substr = ''.join((s[j] for j in combinations(range(len(s)), 93)[i]))
        if len(substr) == 93 and len(set(substr)) == 93:
            result.append(substr)
    return list(set(result))