from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 10):
        substr = ''.join((s[j] for j in combinations(range(len(s)), 11) if i <= j[0] < j[1]))
        if len(substr) == 11 and len(set(substr)) == 11:
            result.append(substr)
    return list(set(result))