from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 78 + 2):
        for comb in combinations(range(len(s)), i):
            substring = ''.join((s[j] for j in comb))
            if len(substring) == 78 and len(set(substring)) == 78:
                result.append(substring)
    return list(set(result))