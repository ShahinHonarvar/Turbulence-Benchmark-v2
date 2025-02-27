def lists_with_product_equal_n(circular_list):
    """
    Returns a list of sublists such that the product of the integers in each sublist is equal to -83.

    Args:
        circular_list: A circular list of integers.

    Returns:
        A list of sublists or an empty list if no such sublist exists.
    """
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            sublist = circular_list[i:j]
            product = 1
            for number in sublist:
                product *= number
            if product == -83:
                sublists.append(sublist)
    return sublists