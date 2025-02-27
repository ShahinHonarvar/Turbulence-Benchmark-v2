from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 24):
        for comb in combinations(s[i:i + 25], 25):
            if len(''.join(set(comb))) == 25:
                result.append(''.join(comb))
    return list(set(result))