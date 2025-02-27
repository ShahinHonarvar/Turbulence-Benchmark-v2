from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 92):
        for comb in combinations(range(len(s)), 93):
            substring = ''.join((s[j] for j in comb if j >= i and j < i + 93))
            if len(substring) == 93 and set(substring) == set(substring):
                result.append(substring)
    return list(set(result))