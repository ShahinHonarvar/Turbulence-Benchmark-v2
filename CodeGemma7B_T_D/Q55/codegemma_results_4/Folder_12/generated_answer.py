def lists_with_product_equal_n(circular_list):
    """
    Returns a list of sublists of contiguous integers from a circular list whose product equals -18.

    Args:
      circular_list: A circular list of integers.

    Returns:
      A list of sublists, or an empty list if no such sublist exists.
    """
    linear_list = circular_list + [circular_list[0]]
    sublists = []
    for i in range(len(linear_list)):
        current_element = linear_list[i]
        product = current_element
        start_index = i
        for j in range(i + 1, len(linear_list)):
            next_element = linear_list[j]
            product *= next_element
            if product == -18:
                sublists.append(linear_list[start_index:j + 1])
            elif product > -18:
                product = current_element
                start_index = j
    return sublists