from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 119):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 120) if j[0] == i))
        if len(substring) == 120 and len(set(substring)) == 120:
            result.append(substring)
    return list(set(result))