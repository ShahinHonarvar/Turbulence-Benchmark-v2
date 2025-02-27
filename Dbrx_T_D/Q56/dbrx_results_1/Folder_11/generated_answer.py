from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 77):
        substr = ''.join((s[j] for j in combinations(range(len(s)), 78)[i]))
        if len(''.join(set(substr))) == 78:
            result.append(substr)
    return list(set(result))