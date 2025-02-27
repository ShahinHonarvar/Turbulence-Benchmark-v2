from math import comb

def find_subset_of_length_n(my_set):
    """Return the number of subsets of size 872 in the given set."""
    n = len(my_set)
    return comb(n, 872)