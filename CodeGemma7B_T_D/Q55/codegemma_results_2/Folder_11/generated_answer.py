def lists_with_product_equal_n(l):
    """
            Input: a circular list of integers.
            Output: a list of contiguously sublists that have product equal to -15.
            """
    result = []
    for i in range(len(l)):
        product = 1
        sublist = []
        for j in range(i, len(l)):
            sublist.append(l[j])
            product *= l[j]
            if product == -15:
                result.append(sublist)
                product = 1
                sublist = []
            elif product > -15:
                break
        if sublist and product == -15:
            result.append(sublist)
    return result