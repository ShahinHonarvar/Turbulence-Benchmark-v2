from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 48):
        for comb in combinations(s[i:i + 49], 49):
            substring = ''.join(comb)
            if len(substring) == len(set(substring)):
                result.append(substring)
    return list(set(result))