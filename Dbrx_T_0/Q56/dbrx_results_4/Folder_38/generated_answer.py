from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 34):
        substr = ''.join((s[j] for j in combinations(range(len(s)), 35)[i]))
        if len(substr) == 35 and len(set(substr)) == 35:
            result.append(substr)
    return list(set(result))