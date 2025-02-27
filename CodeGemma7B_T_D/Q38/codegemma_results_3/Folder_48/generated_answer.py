from itertools import combinations

def find_subset_of_length_n(elements):
    """
    Finds the number of all subsets of a given set of elements of size n.
    """
    return sum((1 for _ in combinations(elements, 793)))