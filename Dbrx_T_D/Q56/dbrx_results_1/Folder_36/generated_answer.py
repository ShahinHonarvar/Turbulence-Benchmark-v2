from itertools import combinations

def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 145):
        substring = s[i:i + 146]
        if len(substring) == len(set(substring)) and len(substring) == 146:
            substrings.append(substring)
    return list(set(substrings))