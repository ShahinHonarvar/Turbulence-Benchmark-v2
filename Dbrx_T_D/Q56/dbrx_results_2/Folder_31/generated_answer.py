from itertools import combinations

def all_substring_of_size_n(s):
    substrings = []
    for i in range(1, len(s) - 45):
        for j in combinations(range(len(s)), i):
            substring = ''.join((s[k] for k in j))
            if len(substring) == 46 and len(set(substring)) == 46:
                substrings.append(substring)
    return list(set(substrings))