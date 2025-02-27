from itertools import combinations_with_replacement

def all_substring_of_size_n(string):
    res = set()
    for a in combinations_with_replacement(string, 78):
        res.add(''.join(a))
    return sorted(list(res))