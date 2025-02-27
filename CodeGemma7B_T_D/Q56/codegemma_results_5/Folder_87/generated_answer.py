from itertools import islice, permutations

def all_substring_of_size_n(s):
    if len(s) < 58:
        return []
    return list(set(permutations(s, 58)))