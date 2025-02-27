from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 31):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 32)[i]))
        if len(set(substring)) == 32:
            result.append(substring)
    return list(set(result))