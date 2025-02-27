from collections import defaultdict

def all_substring_of_size_n(s):
    if len(s) < 30:
        return []
    substrings = defaultdict(set)
    for i in range(len(s) - 29):
        substr = s[i:i + 30]
        substr_set = set(substr)
        if len(substr_set) == 30:
            substrings[len(substrings)].add(substrings)
    return [list(s) for s in substrings.values()]