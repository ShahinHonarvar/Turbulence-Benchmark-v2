from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 97):
        for comb in combinations(range(len(s)), 98):
            substring = ''.join((s[j] for j in comb if j >= i and j < i + 98))
            if len(substring) == 98 and len(set(substring)) == 98 and (substring not in result):
                result.append(substring)
    return result