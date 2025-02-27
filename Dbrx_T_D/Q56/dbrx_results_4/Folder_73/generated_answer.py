from itertools import combinations

def all_substring_of_size_n(s):
    substrings = []
    for i in range(len(s) - 20 + 1):
        substring = ''.join((s[j] for j in sorted(combinations(range(len(s)), 20)[i])))
        if substring not in substrings:
            substrings.append(substring)
    return substrings