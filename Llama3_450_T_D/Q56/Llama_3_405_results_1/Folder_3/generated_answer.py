from itertools import combinations

def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 92):
        substring = s[i:i + 93]
        if len(set(substring)) == 93:
            substrings.add(substring)
    return list(substrings)