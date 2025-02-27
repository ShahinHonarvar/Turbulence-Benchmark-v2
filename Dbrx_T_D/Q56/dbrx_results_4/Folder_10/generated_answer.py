from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 55 + 2):
        substrings = [''.join(comb) for comb in combinations(s[i - 1:i + 54], 55)]
        for substring in substrings:
            if len(substring) == 55 and len(set(substring)) == 55:
                result.append(substring)
    return list(set(result))