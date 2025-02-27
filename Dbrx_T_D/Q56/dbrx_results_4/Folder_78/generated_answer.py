from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    if len(s) < 49:
        return result
    for i in range(len(s) - 48):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 49)[i]))
        if len(set(substring)) == 49:
            result.append(substring)
    return list(set(result))