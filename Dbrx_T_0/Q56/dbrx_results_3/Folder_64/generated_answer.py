from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 7):
        for comb in combinations(s[i:i + 8], 8):
            substring = ''.join(comb)
            if len(substring) == len(set(substring)):
                result.append(substring)
    return list(set(result))