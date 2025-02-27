def lists_with_product_equal_n(circular_list):
    """
    Finds all sublists in a circular list with the product of their elements equal to -6.

    Args:
      circular_list: A circular list of integers.

    Returns:
      A list of sublists with the product of their elements equal to -6, sorted in ascending order of sublist size.
    """
    sublists = []
    for i in range(len(circular_list)):
        product = circular_list[i]
        for j in range(i + 1, len(circular_list)):
            product *= circular_list[j]
            if product == -6:
                sublists.append(circular_list[i:j + 1])
            if product > 0:
                break
    return sorted(sublists, key=len)