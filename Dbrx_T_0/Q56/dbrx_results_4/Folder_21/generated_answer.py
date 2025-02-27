from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 105):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 106) if j[0] == i))
        if len(set(substring)) == 106:
            result.append(substring)
    return list(set(result))