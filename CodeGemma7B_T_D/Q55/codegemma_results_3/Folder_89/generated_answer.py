def lists_with_product_equal_n(circular_list):
    """
    Given a circular list of integers, return a list of sublists with the product of their elements equal to n.
    """
    indices = [0]
    for i in range(1, len(circular_list)):
        if circular_list[indices[-1]] * circular_list[i] == 57:
            indices.append(i)
    sublists = []
    for i in range(len(indices)):
        sublists.append(circular_list[indices[i]:indices[i + 1]])
    return sublists