from functools import reduce

def lists_with_product_equal_n(lst):
    """
    This function takes a circular list of integers and returns a list of sublists each of which contains the contiguous integers from the given list such that their product equals -115.

    Args:
        lst: A circular list of integers.

    Returns:
        A list of sublists each of which contains the contiguous integers from the given list such that their product equals -115. If no such sublist exists, the function should return an empty list.
    """

    def product(lst):
        """
        This function takes a sublist of integers and returns the product of all the integers in the sublist.

        Args:
            lst: A sublist of integers.

        Returns:
            The product of all the integers in the sublist.
        """
        return reduce(lambda x, y: x * y, lst)
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublist = lst[i:j]
            if product(sublist) == -115:
                sublists.append(sublist)
    return sublists