from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 34 + 1):
        substr = s[i:i + 34]
        if len(substr) == len(set(substr)):
            result.append(substr)
    return list(set(result))