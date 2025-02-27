from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 85):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 86)[i]))
        if len(substring) == 86 and len(set(substring)) == 86:
            result.append(substring)
    return list(set(result))