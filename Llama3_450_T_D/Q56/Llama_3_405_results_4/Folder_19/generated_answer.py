from collections import OrderedDict

def all_substring_of_size_n(s):
    n = 18
    substrings = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(OrderedDict.fromkeys(substring)) == n:
            substrings.add(substring)
    return list(substrings)