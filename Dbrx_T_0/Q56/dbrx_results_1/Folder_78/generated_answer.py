from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 47):
        for comb in combinations(s[i:i + 49], 49):
            if len(comb) == len(set(comb)):
                result.append(''.join(comb))
    return list(set(result))