from itertools import combinations_with_replacement

def all_substring_of_size_n(s):
    return list({''.join(c) for c in combinations_with_replacement(s, 39)})