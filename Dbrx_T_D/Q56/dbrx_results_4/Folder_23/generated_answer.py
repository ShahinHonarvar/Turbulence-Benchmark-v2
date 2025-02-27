from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 42 + 1):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 42)))
        if len(substring) == len(set(substring)):
            result.append(substring)
    return list(set(result))