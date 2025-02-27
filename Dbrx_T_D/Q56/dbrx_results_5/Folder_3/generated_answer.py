from itertools import combinations

def all_substring_of_size_n(s):
    substrings = []
    if len(s) < 93:
        return substrings
    for i in range(len(s) - 92):
        for comb in combinations(s[i:i + 93], 93):
            if len(''.join(set(comb))) == 93:
                substrings.append(''.join(comb))
    return list(set(substrings))