from itertools import combinations_with_replacement

def find_subset_of_length_n(s):
    return len(list(combinations_with_replacement(s, 51)))