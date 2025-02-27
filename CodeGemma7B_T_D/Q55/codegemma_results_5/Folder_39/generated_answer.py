from itertools import islice
from functools import reduce

def lists_with_product_equal_n(circular_list):
    """
    Finds contiguous sublists of a circular list with product equal to -46.

    Args:
        circular_list: The circular list of integers.

    Returns:
        A list of sublists with product equal to -46.
    """

    def multiply(x, y):
        return x * y
    result = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            sublist = circular_list[i:j]
            if reduce(multiply, sublist, 1) == -46:
                result.append(sublist)
    return result