from itertools import product

def lists_with_product_equal_n(lst):
    """
    Returns a list of sublists in a circular list that have a product equal to n.

    Args:
        lst: A circular list of integers.

    Returns:
        A list of sublists that have a product equal to n.
    """
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + i + 1):
            sublist = lst[i:j]
            if product(sublist) == -26:
                return [sublist]
        lst.append(lst.pop(0))
    return []