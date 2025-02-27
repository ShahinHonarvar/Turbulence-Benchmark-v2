from itertools import combinations

def find_subsets_of_length_n(my_set, n):
    """Returns the number of all subsets of size n in a set."""
    return sum((1 for subset in combinations(my_set, n)))