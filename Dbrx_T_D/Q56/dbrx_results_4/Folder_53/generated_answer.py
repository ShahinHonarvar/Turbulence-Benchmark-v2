from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 23 + 1):
        for comb in combinations(range(len(s)), i):
            substr = ''.join((s[j] for j in comb))
            if len(substr) == 25 and len(set(substr)) == 25:
                result.append(substr)
    return list(set(result))