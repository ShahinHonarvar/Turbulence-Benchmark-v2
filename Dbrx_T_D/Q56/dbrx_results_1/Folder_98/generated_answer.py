from itertools import combinations

def all_substring_of_size_n(s):
    if len(s) < 10:
        return []
    result = []
    for i in range(len(s) - 9):
        sub = s[i:i + 10]
        if len(set(sub)) == 10:
            result.append(sub)
    return list(set(result))