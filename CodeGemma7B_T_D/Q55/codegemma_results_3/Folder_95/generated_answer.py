from itertools import product, combinations
from math import prod
    from the given list such that their product equals 28.

def lists_with_product_equal_n(circular_list):
    """
    Returns a list of sublists each of which contains the contiguous integers

    Each sublist in the returned list can be of any size as long as it
    is smaller than or equal to the size of the given list.

    If no such sublist exists, the function should return an empty list.

    If there are duplicates of such a sublist, they should all be contained
    in the returned list. The order of sublists in the returned list does not
    matter.
    """
    result = []
    n = len(circular_list)
    for i in range(n):
        for j, k in combinations(range(i + 1, n + i), 2):
            sublist = circular_list[i:k + 1]
            if prod(sublist) == 28:
                result.append(sublist)
    return result