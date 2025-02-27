from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 13):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 14)[i]))
        if len(set(substring)) == 14:
            result.append(substring)
    return list(set(result))