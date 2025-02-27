from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 44):
        for j in combinations(range(len(s)), 45):
            if len(s[j[0]:j[0] + 45].replace(s[j[0]:j[0] + 45][i], '').replace(s[j[0]:j[0] + 45][i - 1], '')) == 43:
                result.append(s[j[0]:j[0] + 45])
    return list(set(result))