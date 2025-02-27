from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 2):
        for j in combinations(range(len(s)), 3):
            substring = s[j[0]:j[0] + 3]
            if len(substring) == 3 and len(set(substring)) == 3 and (substring not in result):
                result.append(substring)
    return result