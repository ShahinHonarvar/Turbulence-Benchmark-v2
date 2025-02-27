from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    if len(s) < 58:
        return result
    for i in range(len(s) - 57):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 58)[i]))
        if len(set(substring)) == 58:
            result.append(substring)
    return list(set(result))