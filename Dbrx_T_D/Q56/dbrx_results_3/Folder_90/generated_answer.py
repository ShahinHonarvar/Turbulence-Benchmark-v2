from itertools import combinations

def all_substring_of_size_n(s):
    result = set()
    for comb in combinations(range(len(s)), 130):
        substring = ''.join((s[i] for i in comb))
        if len(substring) == 130 and len(set(substring)) == 130:
            result.add(substring)
    return list(result)