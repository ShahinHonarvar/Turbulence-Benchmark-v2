from itertools import combinations

def all_substring_of_size_n(s):
    substrings = []
    for i in range(1, len(s) - 37):
        window = s[i:i + 38]
        if len(window) == 38 and len(set(window)) == 38:
            substrings.append(window)
    return list(set(substrings))