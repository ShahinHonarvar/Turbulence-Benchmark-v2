from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 95 + 2):
        for comb in combinations(s[i:i + 95], 95):
            if len(comb) == len(set(comb)):
                result.append(''.join(comb))
    return list(set(result))