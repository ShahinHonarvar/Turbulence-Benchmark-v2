from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 77 + 2):
        for comb in combinations(range(len(s)), i):
            substring = ''.join((s[j] for j in comb))
            if len(substring) == 77 and len(set(substring)) == 77:
                result.append(substring)
    return list(set(result))