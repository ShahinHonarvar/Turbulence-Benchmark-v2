from itertools import combinations

def all_substring_of_size_n(s):
    n = 94
    result = []
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if len(substr) == len(set(substr)):
            result.append(substr)
    return list(set(result))