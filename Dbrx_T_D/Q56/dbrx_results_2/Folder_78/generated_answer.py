from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 48):
        substr = ''.join((s[j] for j in combinations(range(len(s)), 49)[i]))
        if len(substr) == 49 and len(set(substr)) == 49:
            result.append(substr)
    return list(set(result))