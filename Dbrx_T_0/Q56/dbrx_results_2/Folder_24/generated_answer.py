from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 51):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 52) if j[0] == i))
        if len(substring) == 52 and len(set(substring)) == 52:
            result.append(substring)
    return list(set(result))