from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 108):
        for comb in combinations(range(len(s)), 110):
            substring = s[comb[i]:comb[i] + 110]
            if len(substring) == len(set(substring)) and substring not in result:
                result.append(substring)
    return result