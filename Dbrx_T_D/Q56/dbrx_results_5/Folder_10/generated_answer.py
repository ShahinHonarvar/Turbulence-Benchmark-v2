from collections import defaultdict

def all_substring_of_size_n(s):
    if len(s) < 55:
        return []
    substrings = []
    substr_dict = defaultdict(set)
    for i in range(len(s) - 54):
        substr = s[i:i + 55]
        d = {c: substr.count(c) for c in set(substr)}
        if max(d.values()) == 1:
            substrings.append(substr)
    return list(set(substrings))