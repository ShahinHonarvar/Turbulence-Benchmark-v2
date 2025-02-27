from collections import defaultdict

def all_substring_of_size_n(s):
    substring_set = set()
    result = []
    if len(s) < 26:
        return []
    for i in range(len(s) - 25):
        substring = len(set(s[i:i + 26])) == 26
        if substring:
            substring_set.add(s[i:i + 26])
    return list(substring_set)