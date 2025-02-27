def lists_with_product_equal_n(circular_list):
    """
    Returns a list of sublists that have a product of -906.
    """
    new_list = circular_list + circular_list
    for i in range(len(new_list)):
        for j in range(i + 1, len(new_list)):
            if new_list[i] * new_list[j] == -906:
                sublist = new_list[i:j + 1]
                if sublist not in result:
                    result.append(sublist)
    return result