from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, min(106, len(s)) + 1):
        for comb in combinations(range(len(s)), i):
            if len(set((s[pos] for pos in comb))) == i:
                result.append(''.join((s[pos] for pos in comb)))
    return list(set(result))