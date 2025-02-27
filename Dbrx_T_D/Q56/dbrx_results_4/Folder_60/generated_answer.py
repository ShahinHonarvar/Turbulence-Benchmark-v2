from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 35):
        substring = ''.join((s[j] for j in combinations(range(i, len(s)), 36)))
        if len(set(substring)) == 36:
            result.append(substring)
    return list(set(result))