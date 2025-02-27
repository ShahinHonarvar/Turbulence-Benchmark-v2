from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 51):
        for comb in combinations(range(i, i + 52), 52):
            substring = ''.join((s[j] for j in comb))
            if len(set(substring)) == 52:
                result.append(substring)
    return list(set(result))