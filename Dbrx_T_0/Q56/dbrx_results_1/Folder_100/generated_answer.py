from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 91):
        for comb in combinations(range(len(s)), 92):
            substring = ''.join((s[j] for j in comb if j >= i and j < i + 92))
            if len(substring) == 92 and len(set(substring)) == 92 and (substring not in result):
                result.append(substring)
    return result