from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 80):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 81)[i]))
        if len(substring) == 81 and len(set(substring)) == 81:
            result.append(substring)
    return list(set(result))