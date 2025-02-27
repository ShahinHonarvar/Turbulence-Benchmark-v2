from itertools import combinations_with_replacement

def all_substring_of_size_n(str):
    return list(set(combinations_with_replacement(str, 57)))