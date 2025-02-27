import math

def find_subset_of_length_n(my_set):
    """
    Calculate the number of subsets of size 860 in a given set.

    Args:
        my_set (set): The input set of elements.

    Returns:
        int: The number of subsets of size 860 in the given set.
    """
    n = len(my_set)
    return math.comb(n, 860)