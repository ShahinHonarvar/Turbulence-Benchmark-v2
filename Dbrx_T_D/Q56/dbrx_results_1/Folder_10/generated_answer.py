from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 54):
        for j in combinations(range(len(s)), i):
            substring = ''.join((s[k] for k in j))
            if len(substring) == 55 and len(set(substring)) == 55:
                result.append(substring)
    return list(set(result))