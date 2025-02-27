from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 24):
        substr = ''.join((s[j] for j in combinations(range(len(s)), 25)[i]))
        if len(substr) == 25 and len(set(substr)) == 25:
            result.append(substr)
    return list(set(result))