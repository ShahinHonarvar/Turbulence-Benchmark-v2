from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 119):
        for comb in combinations(range(len(s)), 120):
            substr = ''.join((s[j] for j in comb if j >= i and j < i + 120))
            if len(substr) == 120 and substr not in result:
                result.append(substr)
    return result