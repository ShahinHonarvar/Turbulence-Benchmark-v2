from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 144 + 1):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 144) if i <= j[0] < j[1]))
        if len(substring) == 144 and len(set(substring)) == 144:
            result.append(substring)
    return list(set(result))