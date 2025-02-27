from itertools import combinations_with_replacement

def all_substring_of_size_n(str):
    return [''.join(c) for c in combinations_with_replacement(str, 15) if len(set(c)) == 15]