def lists_with_product_equal_n(circular_list):
    """
    This function takes a circular list of integers and returns a list of sublists
    each of which contains the contiguous integers from the given list such that
    their product equals 85. Each sublist in the returned list can be of any size
    as long as it is smaller than or equal to the size of the given list. If no
    such sublist exists, the function should return an empty list. If there are
    duplicates of such a sublist, they should all be contained in the returned
    list. The order of sublists in the returned list does not matter.
    """
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            sublist = circular_list[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == 85:
                sublists.append(sublist)
    return sublists