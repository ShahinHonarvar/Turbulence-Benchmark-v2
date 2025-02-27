from itertools import combinations

def all_substring_of_size_n(s):
    if len(s) < 44:
        return []
    substring_set = set()
    for i in range(len(s) - 43):
        substring = ''.join((s[j] for j in combinations(range(len(s)), 44)[i]))
        if len(substring) == 44 and len(set(substring)) == 44:
            substring_set.add(substring)
    return list(substring_set)