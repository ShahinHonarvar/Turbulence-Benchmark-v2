from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 14):
        for j in combinations(range(len(s)), 15):
            substring = ''.join((s[k] for k in j if k in range(i, i + 15)))
            if len(substring) == 15 and len(set(substring)) == 15:
                result.append(substring)
    return list(set(result))