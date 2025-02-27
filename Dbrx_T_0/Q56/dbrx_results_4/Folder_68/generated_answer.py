from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 74):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 75)[i]))
        if len(substring) == 75 and len(set(substring)) == 75:
            result.append(substring)
    return list(set(result))