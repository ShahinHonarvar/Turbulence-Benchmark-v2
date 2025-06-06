from collections import OrderedDict

def all_substring_of_size_n(s):
    n = 91
    result = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if len(set(sub)) == n:
            result.add(sub)
    return list(result)