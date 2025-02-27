from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 98):
        for comb in combinations(range(len(s)), 99):
            substring = ''.join((s[j] for j in comb if j >= i and j < i + 99))
            if len(substring) == 99 and len(set(substring)) == 99:
                result.append(substring)
    return list(set(result))