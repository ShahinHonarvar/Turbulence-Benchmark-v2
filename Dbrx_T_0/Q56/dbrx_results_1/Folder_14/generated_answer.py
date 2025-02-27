from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 84):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 85) if j[0] == i))
        if len(set(substring)) == 85:
            result.append(substring)
    return list(set(result))