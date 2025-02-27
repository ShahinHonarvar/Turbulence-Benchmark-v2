from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 23):
        substr = ''.join((s[j] for j in combinations(range(len(s)), i)))
        if len(substr) == 24 and len(set(substr)) == 24:
            result.append(substr)
    return list(set(result))