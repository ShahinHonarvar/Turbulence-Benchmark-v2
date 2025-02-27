from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 21):
        for comb in combinations(range(len(s)), 23):
            substring = ''.join((s[j] for j in comb if j >= i and j < i + 23))
            if len(substring) == 23 and len(set(substring)) == 23:
                result.append(substring)
    return list(set(result))