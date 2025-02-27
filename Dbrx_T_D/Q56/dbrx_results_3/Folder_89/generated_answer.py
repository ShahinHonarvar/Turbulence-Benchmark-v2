from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, min(38, len(s)) - 37):
        for comb in combinations(range(len(s)), i):
            substring = ''.join((s[j] for j in comb))
            if len(substring) == 38 and len(set(substring)) == 38:
                result.append(substring)
    return list(set(result))