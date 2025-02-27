from itertools import combinations

def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 1):
        if len(set(s[i:i + 2])) == 2:
            substrings.append(s[i:i + 2])
    return list(set(substrings))