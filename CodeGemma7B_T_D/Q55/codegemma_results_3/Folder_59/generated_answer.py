def lists_with_product_equal_n(circ_list):
    """
    Returns a list of sublists such that the product of the integers in each sublist is equal to a given number.
    """
    result = []
    cur_list = []
    cur_prod = 1
    i = 0
    while i < len(circ_list):
        cur_list.append(circ_list[i])
        cur_prod *= circ_list[i]
        if cur_prod == -3 and len(cur_list) <= len(circ_list):
            result.append(cur_list[:])
        elif cur_prod > -3:
            cur_prod //= cur_list.pop(0)
        i += 1
    return result