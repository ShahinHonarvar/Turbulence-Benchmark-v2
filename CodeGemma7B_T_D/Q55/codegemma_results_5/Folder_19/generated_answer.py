from itertools import combinations_with_replacement

def lists_with_product_equal_n(circ_list):
    """
    Returns a list of sublists from the given circular list whose product is equal to -54.

    Args:
        circ_list: A circular list of integers.

    Returns:
        A list of sublists with the product equal to -54, or an empty list if there are no such sublists.
    """
    sublists = set()
    for i in range(len(circ_list)):
        for j in range(i + 1, len(circ_list) + 1):
            sublist = circ_list[i:j]
            if product(sublist) == -54:
                sublists.add(sublist)
    return list(sublists)

def product(lst):
    """
    Returns the product of elements in the given list.

    Args:
        lst: A list of integers.

    Returns:
        The product of elements in the list.
    """
    prod = 1
    for num in lst:
        prod *= num
    return prod