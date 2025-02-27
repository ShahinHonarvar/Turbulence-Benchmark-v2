from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 16):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 17)[i]))
        if len(substring) == 17 and len(set(substring)) == 17:
            result.append(substring)
    return list(set(result))