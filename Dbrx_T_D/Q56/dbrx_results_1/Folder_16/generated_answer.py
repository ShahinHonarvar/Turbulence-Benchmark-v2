from collections import defaultdict

def all_substring_of_size_n(s):
    if len(s) < 124:
        return []
    substring_map = defaultdict(set)
    for i in range(len(s) - 123):
        substring = s[i:i + 124]
        char_set = set(substring)
        if len(char_set) == 124:
            substring_map[frozenset(char_set)].add(substring)
    result = [list(substrings)[0] for substrings in substring_map.values()]
    return result