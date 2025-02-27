from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 70 + 1):
        substr = s[i:i + 70]
        if len(substr) == len(set(substr)):
            result.append(s[i:i + 70])
    return list(set(result))