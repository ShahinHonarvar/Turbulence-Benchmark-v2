from itertools import combinations

def all_substring_of_size_n(s):
    result = set()
    for c in combinations(s, 124):
        result.add(''.join(c))
    return list(result)