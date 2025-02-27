from itertools import combinations_with_replacement

def find_subset_of_length_n(elements):
    return len(list(combinations_with_replacement(elements, 300)))