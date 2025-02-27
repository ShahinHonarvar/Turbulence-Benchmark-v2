from itertools import combinations_with_replacement

def all_substring_of_size_n(s):
    inp = list(combinations_with_replacement(s, 64))
    return list(set(inp))