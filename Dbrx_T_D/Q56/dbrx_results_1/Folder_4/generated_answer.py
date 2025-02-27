from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 40):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 41)[i]))
        if len(set(substring)) == 41:
            result.append(substring)
    return list(set(result))