from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 95):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 96)[i]))
        if len(substring) == 96 and len(set(substring)) == 96:
            result.append(substring)
    return list(set(result))