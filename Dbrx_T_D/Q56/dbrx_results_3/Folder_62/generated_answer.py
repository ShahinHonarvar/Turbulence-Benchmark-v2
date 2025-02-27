from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 31):
        substr = ''.join((s[j] for j in combinations(range(len(s)), 32)[i]))
        if len(substr) == 32 and len(set(substr)) == 32:
            result.append(substr)
    return list(set(result))