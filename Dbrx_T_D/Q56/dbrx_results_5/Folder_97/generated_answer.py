from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 141):
        substr = ''.join((s[j] for j in combinations(range(len(s)), 142)[i]))
        if len(substr) == 142 and len(set(substr)) == 142:
            result.append(substr)
    return list(set(result))