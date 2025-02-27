from itertools import combinations_with_replacement, product

def lists_with_product_equal_n(circular_list):
    """
    Returns a list of sublists with product equal to -61.

    Args:
        circular_list: A circular list of integers.

    Returns:
        A list of sublists with product equal to -61, or an empty list if no such sublist exists.
    """
    sublists = []
    for start in range(len(circular_list)):
        for end in range(start + 2, len(circular_list) + 1):
            sublist = circular_list[start:end]
            if product(sublist) == -61:
                sublists.append(sublist)
    return sublists