from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 14):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 15) if j[0] == i))
        if len(substring) == 15 and len(set(substring)) == 15:
            result.append(substring)
    return list(set(result))