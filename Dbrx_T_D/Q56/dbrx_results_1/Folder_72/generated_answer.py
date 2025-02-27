from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    n = 88
    if len(s) < n:
        return result
    for i in range(len(s) - n + 1):
        substring = ''.join((s[j] for j in combinations(range(len(s)), n) if j[0] == i))
        if len(substring) == n and len(set(substring)) == n and (substring not in result):
            result.append(substring)
    return result