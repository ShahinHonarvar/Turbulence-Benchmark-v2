from itertools import combinations

def find_subset_of_length_n(s, n):
    """
    This function takes a set s and an integer n and returns the number of all subsets of s of size n.
    
    Arguments:
    s -- set of elements
    n -- size of the subsets

    Returns:
    number of subsets of size n
    """
    return len(list(combinations(s, n)))