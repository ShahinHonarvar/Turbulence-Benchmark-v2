from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 60):
        for comb in combinations(range(len(s)), 61):
            substring = ''.join((s[j] for j in comb if i <= j < i + 61))
            if len(substring) == 61 and len(set(substring)) == 61:
                result.append(substring)
    return list(set(result))