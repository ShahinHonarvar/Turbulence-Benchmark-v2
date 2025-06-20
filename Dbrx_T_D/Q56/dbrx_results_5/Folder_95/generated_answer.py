from itertools import combinations

def all_substring_of_size_n(s):
    n = 89
    subs = []
    if len(s) < n:
        return []
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if len(substr) == len(set(substr)):
            subs.append(substr)
    return list(set(subs))