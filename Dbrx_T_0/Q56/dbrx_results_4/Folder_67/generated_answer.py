from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 42):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 43)[i]))
        if len(substring) == 43 and len(set(substring)) == 43:
            result.append(substring)
    return list(set(result))