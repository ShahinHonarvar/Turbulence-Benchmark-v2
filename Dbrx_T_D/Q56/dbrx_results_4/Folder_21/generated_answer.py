from itertools import combinations

def all_substring_of_size_n(s):
    n = 106
    if len(s) < n:
        return []
    substrs = set()
    for i in range(len(s) - n + 1):
        substr = ''.join(sorted(s[i:i + n]))
        if len(substr) == n:
            substrs.add(substr)
    return list(substrs)