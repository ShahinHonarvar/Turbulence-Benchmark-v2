from collections import defaultdict

def all_substring_of_size_n(s):
    if len(s) < 63 or len(set(s)) != len(s):
        return []
    substrings = set()
    for i in range(len(s) - 62):
        substring = s[i:i + 63]
        substrings.add(substring)
    return list(substrings)