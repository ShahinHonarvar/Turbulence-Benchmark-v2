from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    if len(s) < 124:
        return result
    for i in range(len(s) - 123):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 124) if abs(j - i) <= 123))
        if len(substring) == 124 and len(set(substring)) == 124:
            result.append(substring)
    return list(set(result))