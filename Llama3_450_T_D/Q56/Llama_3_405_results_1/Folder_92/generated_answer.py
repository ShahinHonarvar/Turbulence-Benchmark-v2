from collections import OrderedDict

def all_substring_of_size_n(s):
    substrings = set()
    seen = set()
    n = 9
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) == n and substring not in seen:
            seen.add(substring)
            substrings.add(substring)
    return list(substrings)