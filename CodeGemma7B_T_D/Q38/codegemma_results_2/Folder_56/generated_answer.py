from itertools import combinations

def find_subset_of_length_n(set_of_elements):
    """
    Return the number of all subsets of size 60 of a set.
    """
    return len(list(combinations(set_of_elements, 60)))