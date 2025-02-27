def lists_with_product_equal_n(circular_list, n=-75):
    """
    This function takes a circular list of integers and an optional argument 'n', which defaults to -75.
    It returns a list of sublists of the circular list having a product of 'n'.
    """
    sublists = []
    for i in range(len(circular_list)):
        product = circular_list[i]
        sublist = [circular_list[i]]
        for j in range(i + 1, len(circular_list)):
            product *= circular_list[j]
            sublist.append(circular_list[j])
            if product == n:
                sublists.append(sublist)
            elif product > n:
                break
    return sublists