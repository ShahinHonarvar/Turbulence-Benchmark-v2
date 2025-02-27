from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 32 + 1):
        for comb in combinations(range(len(s)), 34):
            substring = ''.join((s[j] for j in comb if j >= i and j < i + 34))
            if len(substring) == 34 and len(set(substring)) == 34:
                result.append(substring)
    return list(set(result))