from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    if len(s) < 142:
        return result
    for i in range(len(s) - 141):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 142)[i]))
        if len(substring) == 142 and len(set(substring)) == 142:
            result.append(substring)
    return list(set(result))