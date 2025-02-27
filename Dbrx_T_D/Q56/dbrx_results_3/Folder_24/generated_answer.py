from itertools import combinations

def all_substring_of_size_n(s):
    substrings = []
    for i in range(1, min(52, len(s)) + 1):
        for j in combinations(range(len(s)), i):
            substring = ''.join((s[k] for k in j))
            if len(set(substring)) == len(substring):
                substrings.append(substring)
    return list(set(substrings))