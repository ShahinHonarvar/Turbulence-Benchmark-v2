from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    if len(s) < 75:
        return result
    for i in range(len(s) - 74):
        subset = s[i:i + 75]
        if len(set(subset)) == 75:
            result.append(subset)
    return list(set(result))