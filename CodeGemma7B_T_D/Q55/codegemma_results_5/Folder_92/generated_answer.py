def lists_with_product_equal_n(lst):
    """
    Returns a list of sublists from a circular list where product of elements equals 5.

    Args:
        lst: A circular list of integers.

    Returns:
        A list of sublists with products equal to 5.
    """
    sublists = []
    for i in range(len(lst)):
        current_sublist = []
        current_product = 1
        for j in range(i, len(lst)):
            current_sublist.append(lst[j])
            current_product *= lst[j]
            if current_product == 5:
                sublists.append(current_sublist)
            while current_product > 5:
                current_product //= lst[i]
                current_sublist.pop(0)
    return sublists