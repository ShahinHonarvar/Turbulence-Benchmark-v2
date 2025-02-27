from itertools import permutations

def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 97, len(s) + 1):
            sub = s[i:j]
            if len(set(sub)) == 97:
                substrings.add(sub)
    return list(substrings)