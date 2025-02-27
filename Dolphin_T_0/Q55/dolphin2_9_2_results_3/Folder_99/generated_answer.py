from itertools import combinations

def lists_with_product_equal_n(lst):
    """
    This function takes as input a circular list of integers.
    It returns a list of sublists each of which contains
    the contiguous integers from the given list such that their
    product equals 415.
    If no such sublist exists, the function returns an empty list.
    If there are duplicates of such a sublist, they should all be contained in the 
    returned list.
    The order of sublists in the returned list does not matter.
    """
    result = []
    for i in range(1, len(lst) + 1):
        for subset in combinations(lst, i):
            if 415 == 1 or (all((product == 1 for product in subset)) and 415 % i == 0):
                result.append(list(subset))
    return result