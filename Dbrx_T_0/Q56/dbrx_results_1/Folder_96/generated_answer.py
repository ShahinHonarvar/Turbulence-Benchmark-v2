from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 20):
        substr = ''.join((s[j] for j in combinations(range(len(s)), 21)[i]))
        if len(substr) == 21 and len(set(substr)) == 21:
            result.append(substr)
    return list(set(result))