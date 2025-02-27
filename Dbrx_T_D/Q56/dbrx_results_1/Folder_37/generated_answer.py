from itertools import combinations

def all_substring_of_size_n(s):
    if len(s) < 65:
        return []
    result = []
    for i in range(len(s) - 64):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 65)[i]))
        if len(set(substring)) == 65:
            result.append(substring)
    return list(set(result))