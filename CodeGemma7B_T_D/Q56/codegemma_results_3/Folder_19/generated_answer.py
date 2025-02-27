from itertools import combinations_with_replacement

def all_substring_of_size_n(s):
    return [''.join(p) for p in combinations_with_replacement(s, 18) if len(set(p)) == 18]