from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 83):
        for comb in combinations(range(len(s)), 84):
            substring = ''.join((s[j] for j in comb if j >= i and j < i + 84))
            if len(substring) == 84 and len(set(substring)) == 84:
                result.append(substring)
    return list(set(result))