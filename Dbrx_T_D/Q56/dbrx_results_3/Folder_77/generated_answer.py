from itertools import combinations

def all_substrings_of_size_n(s):
    result = []
    for i in range(len(s) - 144 + 1):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 144) if j[0] == i))
        if len(set(substring)) == 144:
            result.append(substring)
    return list(set(result))