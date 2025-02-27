from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 44):
        for comb in combinations(range(len(s)), 45):
            substring = ''.join((s[j] for j in comb if j >= i and j < i + 45))
            if len(substring) == 45 and len(set(substring)) == 45 and (substring not in result):
                result.append(substring)
    return result