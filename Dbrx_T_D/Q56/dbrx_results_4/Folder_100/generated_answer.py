from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    if len(s) < 92:
        return result
    for i in range(len(s) - 91):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 92)[i]))
        if len(substring) == 92 and len(set(substring)) == 92:
            result.append(substring)
    return list(set(result))