from itertools import combinations

def lists_with_product_equal_n(circular_list, target=74):
    """
    Returns a list of sublists from a circular list of integers such that the product of the integers in each sublist equals the target value.

    Args:
        circular_list: A circular list of integers.
        target: The target product value.

    Returns:
        A list of sublists with the product of the integers in each sublist equal to the target value.
    """
    return [sublist for sublist in combinations(circular_list, len(circular_list)) if product_of_list(sublist) == target]

def product_of_list(lst):
    """
    Returns the product of the integers in a given list.

    Args:
        lst: A list of integers.

    Returns:
        The product of the integers in the list.
    """
    product = 1
    for num in lst:
        product *= num
    return product